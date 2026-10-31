#!/usr/bin/env node
/**
* convert-to-zhtw.mjs
*
* Convert this repository (mirrored from RongleCat/grok-bot-learn, Simplified
* Chinese) into Taiwan Traditional Chinese (zh-TW) in place, using
* @willh/opencc-cli (config: cn -> tw2), then patch the VitePress site config
* for GitHub Pages deployment under doggy8088/grok-bot-learn.
*
* Usage:
* npm install -g @willh/opencc-cli
* node scripts/convert-to-zhtw.mjs
*
* Environment:
* OPENCC_BIN - opencc-cli binary name/path (default: "opencc-cli")
* OPENCC_FROM - source locale (default: "cn")
* OPENCC_TO - target locale (default: "tw2")
*
* Notes:
* - Only text files that actually contain CJK characters are converted.
* - Binary assets, lock files,.git, node_modules, build output, and this
* automation itself (.github/, scripts/) are left untouched.
*/
import { spawnSync} from 'node:child_process';
import {
readdirSync,
readFileSync,
statSync,
writeFileSync,
chmodSync,
renameSync,
existsSync,
} from 'node:fs';
import { join, extname, sep} from 'node:path';

const ROOT = process.cwd();
const BIN = process.env.OPENCC_BIN || 'opencc-cli';
const FROM = process.env.OPENCC_FROM || 'cn';
const TO = process.env.OPENCC_TO || 'tw2';

const PAGES_ORIGIN = 'https://grok-bot-learn.gh.miniasp.com';
const PAGES_BASE = '/';
const PAGES_SITE = PAGES_ORIGIN + PAGES_BASE.replace(/\/$/, '');

const SKIP_DIRS = new Set([
'.git',
'node_modules',
'dist',
'cache',
'.vitepress', // handled carefully below: only dist/cache inside are skipped via name check
'.github',
'scripts',
]);
const SKIP_FILES = new Set(['package-lock.json']);
const TEXT_EXTS = new Set([
'.md', '.txt', '.json', '.html', '.htm', '.vue', '.ts', '.mts', '.cts',
'.js', '.mjs', '.cjs', '.css', '.scss', '.py', '.sh', '.bash', '.yml',
'.yaml', '.toml', '.svg', '.xml', '.csv',
]);
const CJK = /[\u3400-\u9fff\uf900-\ufaff]/;

function* walk(dir) {
for (const entry of readdirSync(dir, { withFileTypes: true})) {
const full = join(dir, entry.name);
if (entry.isDirectory()) {
if (entry.name === 'node_modules' || entry.name === '.git' ||
entry.name === '.github' || entry.name === 'scripts' ||
entry.name === 'dist' || entry.name === 'cache') continue;
yield* walk(full);
} else if (entry.isFile()) {
yield full;
}
}
}

function isTextCandidate(file) {
const base = file.split(sep).pop();
if (SKIP_FILES.has(base)) return false;
const ext = extname(base).toLowerCase();
if (TEXT_EXTS.has(ext)) return true;
if (!ext) {
// Extensionless files (e.g. LICENSE): treat as text if no NUL bytes.
const buf = readFileSync(file);
return!buf.includes(0);
}
return false;
}

function convertFile(file) {
const tmp = file + '.opencc-tmp';
const res = spawnSync(BIN, ['-f', FROM, '-t', TO, '-i', file, '-o', tmp], {
encoding: 'utf8',
maxBuffer: 64 * 1024 * 1024,
});
if (res.status!== 0) {
throw new Error(`opencc-cli failed for ${file}: ${res.stderr || res.stdout || res.error}`);
}
const mode = statSync(file).mode;
renameSync(tmp, file);
chmodSync(file, mode);
}

// --- 1. Convert all CJK text files -------------------------------------------
let converted = 0;
let scanned = 0;
for (const file of walk(ROOT)) {
if (!isTextCandidate(file)) continue;
scanned++;
const content = readFileSync(file, 'utf8');
if (!CJK.test(content)) continue;
convertFile(file);
converted++;
}
console.log(`[convert] scanned ${scanned} text files, converted ${converted} files (${FROM} -> ${TO})`);

// --- 2. Patch VitePress config for zh-TW + GitHub Pages ----------------------
const configPath = join(ROOT, 'site', 'docs', '.vitepress', 'config.mts');
if (existsSync(configPath)) {
let cfg = readFileSync(configPath, 'utf8');
const before = cfg;
// Canonical origin / sitemap / OG URLs -> GitHub Pages site
cfg = cfg.replaceAll('https://bot.fmcat.top', PAGES_SITE);
// Language tags
cfg = cfg.replaceAll('zh-CN', 'zh-TW').replaceAll('zh_CN', 'zh_TW');
// Project Pages base path (skip if already present)
if (!/base:\s*['"]\//.test(cfg)) {
cfg = cfg.replace('defineConfig({', `defineConfig({\n base: '${PAGES_BASE}',`);
}
if (cfg!== before) {
writeFileSync(configPath, cfg);
console.log('[convert] patched site/docs/.vitepress/config.mts (SITE, lang, base)');
} else {
console.log('[convert] config.mts already patched, skipped');
}
} else {
console.warn('[convert] WARNING: VitePress config not found, skipped patching');
}

// --- 3. Credit original author & translator in the site footer ----------------
// SiteFooter.vue is mounted in the layout-bottom slot, so it shows on every
// page. Text here is written directly in Traditional Chinese (this script
// itself is excluded from conversion).
const footerPath = join(ROOT, 'site', 'docs', '.vitepress', 'theme', 'SiteFooter.vue');
if (existsSync(footerPath)) {
  let footer = readFileSync(footerPath, 'utf8');
  if (!footer.includes('tz-credit')) {
    const credit = '      <p class="tz-credit">原作者：<a href="https://github.com/RongleCat/grok-bot-learn" target="_blank" rel="noopener">鐵柱AGI</a>｜繁體中文翻譯：<a href="https://www.facebook.com/will.fans/" target="_blank" rel="noopener">Will 保哥</a></p>\n';
    footer = footer.replace(/(?=<p class="tz-note">)/, credit);
    const creditCss = [
      '.tz-credit {',
      '  margin: 0;',
      '  font-size: 13px;',
      '  line-height: 20px;',
      '  color: var(--vp-c-text-2);',
      '}',
      '.tz-credit a {',
      '  color: inherit;',
      '  font-weight: 500;',
      '  text-decoration: none;',
      '  transition: color 0.2s;',
      '}',
      '.tz-credit a:hover {',
      '  color: #2563eb;',
      '}',
      '',
    ].join('\n');
    footer = footer.replace(/(?=\.tz-note \{)/, creditCss);
    writeFileSync(footerPath, footer);
    console.log('[convert] added author/translator credit to SiteFooter.vue');
  } else {
    console.log('[convert] footer credit already present, skipped');
  }
} else {
  console.warn('[convert] WARNING: SiteFooter.vue not found, skipped footer credit');
}

// --- 4. Prepend a zh-TW notice to README.md -----------------------------------
const readmePath = join(ROOT, 'README.md');
if (existsSync(readmePath)) {
const readme = readFileSync(readmePath, 'utf8');
if (!readme.includes('每日自動同步上游')) {
const notice = [
'> 本分支（zh-tw）由 GitHub Actions 每日自動同步上游 [RongleCat/grok-bot-learn](https://github.com/RongleCat/grok-bot-learn) 的 main 分支，並以 [@willh/opencc-cli](https://www.npmjs.com/package/@willh/opencc-cli) 將全站內容轉換為台灣繁體中文後發佈。簡體原文請見本 repo 的 main 分支。網站：https://grok-bot-learn.gh.miniasp.com/',
'',
'',
].join('\n');
writeFileSync(readmePath, notice + readme);
console.log('[convert] prepended zh-TW notice to README.md');
}
}

console.log('[convert] done');
