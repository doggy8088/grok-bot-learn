# Chapter 23 Team and Enterprise Deployment

When deploying Grok Bot for a team, common blockers typically include the following:

- Gateways intercepting during the handshake phase, causing **cloud computers to fail to connect**.
- Linux VMs without an MDM client installed, causing enterprise IdPs to classify them as untrusted devices.
- Risks of credential leakage and intranet penetration, along with a lack of silent client distribution methods.

By configuring **SSO and security gateway exemptions** according to the process and establishing private network access, you can master batch lifecycle management.


![Team and Enterprise Deployment](/info/23-enterprise.png)

## Team and Enterprise Administrative Controls: Architecture and Capability Boundaries

![Team and Enterprise Administrative Controls: Architecture and Capability Boundaries](/info/23-enterprise-s1.png)

### What It Is

**Each user has a dedicated cloud Firecracker microVM**, issuing instructions and approvals locally while code and browsers run in the cloud.

A heads-up on a common pitfall: **all Bots under a user's account share this single VM**, and files and login states are fully interoperable.

The 2026-10-12 The X Subscription plan divides permissions into two editions:

- **Team Edition**: Enabled for all members by default, uses a shared static egress IP, and includes basic auditing and team rules.
- **Enterprise Edition**: Supports group-based authorization and SCIM 2.0, allows sudo and network allowlists, and includes operation recording and OpenTelemetry export (tagged with `cursor.surface=grok_bot`).

See documentation at [Grok Bot for Teams and Enterprise](https://cursor.com/cn/docs/grok-bot/teams).

### How to Do It

Daily configuration is handled on the [Grok Bot page of the Cursor Dashboard](https://cursor.com/dashboard/bot), mainly in four steps.

1. Divide permissions and basic toggles
- During the rollout phase, click **Manage Group Access** to select pilot groups; disable Cloud Agents if cloud coding is not needed; keep public template sharing disabled to prevent leaks.
- **Local execution is recommended to be set to Never allow**, while disabling local egress routing to prevent detour forwarding.
- For sidebar Bots, select All team or specify groups in the Auto-add column to pin them.

2. Configure approval locks and rules
- Enable **Enforce Auto-review mode**, so members cannot disable review on their own in the client.
- Set high-risk operations such as production deployments or sending external emails to Ask first, and limit read-only operations to Allow automatically.
- **When team rules conflict with personal rules, the system strictly enforces Ask first as the priority**.

3. Set up network and secrets
- Set the network to Team allowlist only or add default values, specifying domain names and IP ranges; disable sudo (enabled by default) to prevent system tampering.
- **Teams can add up to 100 Team Secrets**, with a single secret limit of 32 KB and a total capacity limit of 96 KB; plaintext is not displayed after saving.
- Secret variable names are prohibited from using system reserved names such as `PATH`, `HOME`, and prefixes starting with `SAND_` or `LD_`.

4. Configure group-level policies
- Access groups from [Members > Groups](https://cursor.com/dashboard/members?subtab=groups). **The configuration principle is that policies can only be relaxed, not restricted further**.
- Check Don't enforce for this group to unlock the auto-review lock.
- Network policy is an exception: group policies directly override team policies. If a member belongs to multiple groups, network policies enforce the strictest rule, while permissions apply the most permissive rule.

### What Good Looks Like

- The dashboard clearly distinguishes between pilot groups and unauthorized groups, and unauthorized personnel cannot activate Bots in the client.
- Team rules and Auto-review rules are locked; members can view team rules in the client settings page, but edit and delete buttons are disabled.
- High-risk operations (external communications, file destruction, privileged commands) trigger approval interception 100% of the time.

---

## Identity and SSO: Enabling Organization-Wide Access and Device Trust Compatibility

### What It Is

Grok Bot inherits the Cursor account system, so **there is no need to create a separate application in the IdP**. Reference documentation: [Configure Identity and Access](https://cursor.com/cn/docs/grok-bot/identity).

Bots run in cloud Linux VMs without MDM installed, so they cannot satisfy FastPass or Hybrid Join requirements. **Remember never to disable device compliance globally**; instead, configure bypass policies for target groups before the block rules.

### How to Do It

- **Expand Okta Assignment**: Go to **Assignments** > **Assign to Groups** in the Cursor app and select business groups; when SCIM is enabled, assign and push groups (Push Groups) simultaneously.

  **Both SAML SSO and SCIM must be assigned simultaneously**; omitting SSO will cause logins to be blocked.
- **Expand Entra ID Assignment**: In the Cursor app under **Users and groups**, click **Add user/group** to add groups (requires P1/P2 license, nested groups are not supported); synchronize and assign the same groups in the provisioning application.
- **Allow Linux in Okta**: Create a new rule `Grok Bot computer (Linux)` before the authentication policy block rules.

  Restrict users to the Cursor group, **set Device platform to Other Desktop** (no dedicated Linux option), and set Device state to Any; select Password + Another factor for verification, leaving phishing-resistant restrictions unchecked.
- **Allow Linux in Entra ID**: Create a high-priority policy specifying the Cursor group and target application; include Linux under Device platforms while excluding Windows and macOS; check Require multifactor authentication under Grant; **the existing compliance policy must exclude this group or the Linux platform**.

### What Good Looks Like

- Business users log into the desktop client using enterprise SSO without encountering `User is not assigned to this application`.
- Accessing the intranet inside the Bot browser via password plus secondary authentication succeeds without FastPass or device non-compliance prompt blocks.
- **When employees access from their personal computers, existing FastPass and device compliance rules remain strictly in effect**.

## Private Network Access: Desktop Routing and Automated Team Setup Scripts

![Private Network Access: Desktop Routing and Automated Team Setup Scripts](/info/23-enterprise-s3.png)

### What It Is

Grok Bot runs in the cloud; **accessing the intranet requires establishing a private network connection**.

- Desktop routing: Suitable for temporary debugging. Enable `Settings > Computer > Route traffic through this computer` in the client; traffic routes through the local network card, and administrators can disable this with one click in the backend.
- Team Setup client installation: For persistent access and **limited to Enterprise Edition only**. IT centrally maintains scripts that automatically launch and join the intranet whenever the Bot starts or refreshes.

For details, see [Connect to Private Networks](https://cursor.com/cn/docs/grok-bot/private-networks).

### How to Do It

Team environment setup scripts are located under **Bot Computers** in the dashboard and run as a non-root user with `sudo` inside the Debian Linux VM. **The script runs at boot and refreshes periodically approximately once per day, with a 30-minute timeout limit**.
- An exit code of 0 for `check` skips installation; after installation completes, `check` runs again for verification.
- **Execution failures do not block computer startup**; retries occur during the next periodic refresh.

#### Tailscale Networking Solution

1. Open **Team Secrets**, add the Tailscale authentication key `TS_AUTHKEY` (value formatted as `tskey-auth-...`), and bind a dedicated ACL tag (such as `tag:grok-bot`) in the Tailscale admin console to **strictly restrict access permissions**.
2. Go to team environment setup scripts, click **+** to create a new manifest, set the Manifest ID to `private-network-tailscale`, and switch to JSON or form mode to enter the configuration:

::: details Tailscale Networking Solution
```json
{
  "manifestId": "private-network-tailscale",
  "entries": [
    {
      "id": "install-tailscale",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://tailscale.com/install.sh | sh\nsudo tailscale up --authkey=\"$TS_AUTHKEY\" --accept-routes --hostname=\"grok-vm-${USER}\"",
      "check": "command -v tailscale && tailscale status"
    }
  ]
}
```
:::

#### Cloudflare Tunnel Solution

- Private HTTP services: Directly access the tunnel routed domain, authenticated by Cloudflare Access with interactive login completed in the Bot browser.
- Private TCP services (such as databases, SSH): Install `cloudflared` in the manifest; run the command in the Shell to **open a local forwarding port** when connecting:

`cloudflared access tcp --hostname db-internal.corp.com --url localhost:5432`

::: details Cloudflare Tunnel Solution
```json
{
  "manifestId": "private-network-cftunnel",
  "entries": [
    {
      "id": "install-cloudflared",
      "setup": "#!/usr/bin/env bash\nset -euo pipefail\ncurl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null\necho 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared bullseye main' | sudo tee /etc/apt/sources.list.d/cloudflared.list\nsudo apt-get update && sudo apt-get install -y cloudflared",
      "check": "command -v cloudflared"
    }
  ]
}
```
:::

#### Coordinating with Network Policies to Allow Control Plane Endpoints

If the team enables **Team allowlist only** network controls, **the control planes of networking tools must be added to the allowlist**; otherwise, clients cannot complete authentication. For example, when using Tailscale, allow coordination servers and DERP relay server domains in the policy; policy changes propagate to virtual machines in about 1 minute.

### What Good Looks Like

- Newly created or recreated Bot computers automatically appear in the Tailscale or Cloudflare admin console device list with an online status after startup completes.
- The `check` script in the manifest consistently returns 0 during subsequent daily periodic refreshes, without repeating installation logic.
- Sensitive tokens are injected entirely via Team Secrets, with no plaintext credentials appearing in manifest text or execution logs.

---

## Proxies and Enterprise Gateway Pitfalls: Allowlist Rules and TLS Inspection Exemptions

Enterprise gateways (such as Zscaler or Palo Alto) frequently cause chats to function normally while **failing to capture screenshots or control terminals**.

The root cause is that the control plane uses HTTP/2 or SSE streaming persistent connections over second-level nested domains `<computer>.<cluster>.cursorvm.com`, which normal single-level rules fail to match.

See official instructions at [Configure TLS Inspection Proxies](https://cursor.com/cn/docs/grok-bot/proxies).

### Key Configuration Points

Gateways must allow the following domains while **disabling response buffering and exempting TLS inspection** to prevent end-to-end handshake failures and streaming timeouts:
- `*.cursor.sh`: Core APIs
- `*.cursorvm.com` and **`*.*.cursorvm.com`**: Control channels; two-level wildcards must be supported
- `*.cursor-cdn.com`, `*.cursorapi.com`, `downloads.cursor.com`, and the main website: Static assets and download updates

After configuring policies, **be sure to synchronize them to Off-Network roaming profiles** to prevent employees from losing connection when working remotely or off-network.

### Device Troubleshooting and Verification

Follow these troubleshooting steps in an employee's computer terminal:

1. Verify whether certificates have been altered; the normal issuer must be **Amazon RSA**:
```bash
   curl -v https://api2.cursor.sh |& grep -C1 issuer:
   ```
2. Verify multi-level DNS resolution; if it fails, compare with `nslookup test.us9.cursorvm.com 1.1.1.1`:
```bash
   nslookup test.us9.cursorvm.com
   ```
3. Check streaming data transmission: Data should output line by line. If it pauses for several seconds and then prints all at once, gateway buffering has not been disabled.

Acceptance criteria: **Both office network and home roaming connect to cloud computers within 5 seconds**, certificates pass through directly to Amazon RSA, and streaming long connections exhibit zero buffering latency.

## Desktop Client Distribution and Version Control

### Platforms and Update Mechanisms

| Platform | Installation Format | Update Logic |
| --- | --- | --- |
| macOS | `.dmg` (Apple Silicon / Intel) | Automatically checks for updates on startup; **disabling via policy is not supported** |
| Windows | Setup `.exe` (x64 / Arm64) | Automatically checks for updates on startup; disabling via policy is not supported |
| Linux | `.deb`, `.rpm`, AppImage | deb and rpm are managed by package managers; AppImage checks for updates automatically |
| iOS | App Store | Requires iOS 18 or later |
| Android | Google Play | Requires Android 9 or later; supports managed push |

See official deployment instructions at [Deploy Grok Bot to Your Organization](https://cursor.com/cn/docs/grok-bot/deployment).

### Deployment and Version Control

1. **Obtain Installation Packages**
   Do not download installation packages manually from web pages; fetch directly from the official JSON feed: `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`.
   `{platform}` supports macOS (`darwin-arm64`, `darwin-x64`), Windows (`win32-x64-user`, `win32-arm64-user`), and Linux (`linux-x64`, `linux-arm64`).
```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/win32-x64-user/sand
```
   The endpoint returns `version`, `commitSha`, `downloadUrl`, as well as `debUrl` and `rpmUrl` for Linux. For macOS and Windows, package URLs can also be constructed directly according to the rules:
   - Windows: `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`
   - macOS: `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`

2. **MDM Push**
   - Windows (Intune / SCCM): Add `/S` as the silent installation parameter. The installer writes to the current user's `%LOCALAPPDATA%\Programs` by default, so **it must run in the User Context**.

     Never use the local SYSTEM account, as it will install to the wrong path and employees will not find the application.
```cmd
  Grok_Bot_1.0.0_Setup.exe /S
  ```
   - macOS (Jamf / Kandji / Intune): Push the `.dmg` matching the architecture to the `/Applications` directory.
   - Linux (Ansible / Puppet): Install the `.deb` or `.rpm` package; the system will automatically configure official package repositories.

3. **Version Control and Pinning**
   macOS and Windows cannot completely disable automatic updates via policy.

Linux versions can be locked via the package manager, or synchronized updates paused by setting `Enabled: no` in `/etc/apt/sources.list.d/grok-bot.sources` or `enabled=0` in `/etc/yum.repos.d/grok-bot.repo`:
```bash
  sudo apt-mark hold grok-bot
  ```
   Cursor establishes support lifetimes for older versions. **Clients below the minimum supported threshold will encounter a full-screen Update required popup that blocks usage**, and pinned Linux versions past this threshold will also be blocked. Operations teams need to **roll out tested new stable releases every two to four weeks**.

### Acceptance Criteria

- Office devices complete silent installation via MDM, so **desktops are ready immediately upon onboarding new employees**.
- The IT team maintains a consistent version rotation cadence, completing internal organizational version upgrades before official cutoffs take effect.

## Managing Bot Computers: Batch Operations and Lifecycle

![Managing Bot Computers: Batch Operations and Lifecycle](/info/23-enterprise-s6.png)

### Core Operations and Permissions

Access this under the **Bot Computers** section of the [Grok Bot page on the Cursor Dashboard](https://cursor.com/dashboard/bot) by clicking **Manage Bot Computers**.

**This feature is restricted to Enterprise Edition Organization Admins**; standard team admins cannot see this entry point.

See documentation at [Manage Grok Bot Computers](https://cursor.com/cn/docs/grok-bot/computers).

| Operation Name | Underlying Behavior | Data and File Retention State | Applicable Scenarios |
| --- | --- | --- | --- |
| **Recreate VMs** | Reinstalls using the latest image and reruns environment scripts | **Retained**. Disk remains intact; Bots, personal files, and cookies are all preserved, only clearing self-installed system software | Applying environment script changes, rolling out new images |
| **Terminate VMs** | Immediately destroys running or hibernated instances, interrupting active compute | **Retained**. Disk is retained; sending a message from the client next time spins up a clean VM | Resolving frozen instances, freeing cloud resource usage |
| **Delete VM and Data** | Destroys the VM and completely deletes underlying bound persistent storage | **Not Retained**. Data is completely wiped; next use re-initializes as a blank computer | Offboarding employee cleanup, complete reset upon data corruption |

### Console Operations and Troubleshooting

1. Enter the page, click **Manage**, and search by name or email to filter members; supports single selection, multiple selection, or **Select all**.
2. Select the target operation in the **Manage selected** dropdown, verify the count of affected users, and execute.
3. After execution finishes, **you must click the Done button on the card**. Each team can only run one batch operation at a time; failing to click Done keeps subsequent action buttons locked.

When encountering skipped or failed statuses, handle them based on the receipts:
- **Skipped (No VM / Operation cannot be completed)**: User has no VM or left the team while queued; no action needed.
- **Failed (Another recreate is in progress / VM scan not completed)**: Another update has not finished or the backend temporarily failed to fetch state; retry after a few minutes.
- **Failed (Operation cannot be completed)**: The Bot is running heavy tasks leading to a timeout; notify the user to let the Bot idle before retrying.

### Automation and Acceptance Criteria

Toggle on the **Terminate Inactive Computers** switch above the action buttons. **Computers inactive for 30 consecutive days will terminate automatically**, freeing compute instances while retaining disks, cleaned up by the system on a rolling schedule.

For multi-team batch operations, invoke the [Organization Admin API](https://cursor.com/docs/account/organizations/organization-admin-api.md#grok-bot-computers).

When calling, provide an Organization API key with `admin:*` permissions, pass the team ID, array of member emails, and action type (`recreate` or `terminate`), and poll for progress—similarly constrained by the single-concurrency-per-team limit.

Focus on two key metrics during acceptance:
- Seamless batch recreation of instances without data loss.
- Enabling 30-day idle auto-termination to prevent zombie VMs from consuming organizational cloud quotas.

## Enterprise Security Baseline Configuration and Practical Prompts

### Administrator Configuration
1. Lock network to "Team allowlist only", and disable public templates and email channels.
2. Enable **Enforce Auto-review**, and set local execution to **Never allow** to prevent unauthorized downgrades.
3. For any actions calling production APIs, modifying databases, sending outbound emails, signing agreements, or merging into `main`, require **Ask first**; allow log queries and compilation automatically.

### Employee Guidelines
1. Pass credentials through environment variables; **never paste plaintext passwords into chat dialogs**.
2. Choose **Allow once** for sensitive authorizations; avoid selecting always allow, and exit promptly when finished.

### Practical Prompts
::: details Practical Prompts
```text
你現在負責對內部服務進行介面與架構調研。
請遵循以下嚴格的安全限制：
1. 本次任務為純唯讀模式，嚴禁對目標服務發起任何 POST、PUT、DELETE 請求。
2. 檢查網路連通性：嘗試向內部端點 http://api-monitor.corp.internal/health 發起 GET 請求並打印狀態碼。
3. 如果遇到證書問題或連線被重定向，記錄錯誤記錄，不要嘗試使用任何提權手段。
4. 將調研結果彙總輸出為 Markdown 表格，包含服務名稱、回應耗時、健康狀態。
5. 完成後暫停執行，等待我的進一步指令，不要擅自讀取其他網段資產。
```
:::

::: details Practical Prompts
```text
請按規範完成本週發版程式碼的對比檢查與 PR 草稿建立：
1. 切換到工作區程式碼目錄，拉取 origin/main 最新分支。
2. 比對 feature/sso-login 分支與 main 分支的改動差異，列出所有變動的文件列表。
3. 檢查是否有硬寫程式的密鑰、密碼或私鑰文件被提交。如果發現任何形如 'AKIA...' 或 'BEGIN PRIVATE KEY' 的文本，立即中斷任務並向我告警。
4. 在本地執行靜態檢查指令碼：npm run lint 和 npm run test。
5. 準備 PR 描述文本草稿，包含變更摘要與測試結果。
6. 注意：嚴禁直接推送到遠端倉庫。把 PR 描述保存為 local-pr-draft.md 後向我申請確認。得到明確授權前不得執行 git push。
```
:::

::: details Practical Prompts
```text
請處理今天未分配的內部支援工單：
1. 打開瀏覽器，訪問內部工單主控台 https://tickets.corp.internal。
2. 過濾出狀態為 'New' 且優先級為 'High' 的所有工單。
3. 逐條提取工單的核心問題，按照以下類別打標記：[帳號登入]、[權限申請]、[網路故障]。
4. 為每條工單生成標準回覆模版，存入草稿區。
5. 涉及權限開通的工單，一律在回覆中註明：'需直屬主管在 OA 提交審批流，當前僅作資訊預審'。
6. 嚴格要求：所有郵件和系統回覆只保留在草稿狀態，嚴禁點選 'Send' 或 'Submit'。生成處理清單供我逐條審查。
```
:::

## Common Pitfalls

1. **Missing multi-level wildcards in gateway**: The hostname is `<vm-id>.<cluster-id>.cursorvm.com`; configuring only `*.cursorvm.com` stalls at 99%, so **`*.*.cursorvm.com` must also be added**.
2. **Proxy buffering truncating streams**: Enabling Response Buffering in Zscaler causes disconnections. **Buffering must be disabled for Cursor domains to pass through Server-Sent Events transparently**.
3. **Missing allowlists in roaming policies**: Inability to connect when working from home is due to Zscaler switching to Off-Network policies. Remember to synchronize domain allowlists and TLS exemptions to off-network profiles.
4. **Accidentally enabling legacy privacy mode**: Enabling "Privacy Mode (Legacy)" in the backend completely disables Bots; turn it off in team settings.
5. **IdP strictly requiring compliant devices**: Cloud Linux VMs are not managed by MDM and cannot run FastPass. **Add high-priority rules for Linux (Other Desktop) in Okta/Entra ID** to allow access via password plus mobile secondary authentication.
6. **Storing secrets in plaintext in scripts**: Team Setup is plaintext JSON. Store tokens in **Team Secrets** and read them in scripts using `"$TS_AUTHKEY"`.
7. **Application missing when installed with SYSTEM privileges**: The program installs into `%LOCALAPPDATA%\Programs`. **The `/S` installation command must be run in the current user context**.
8. **Mistaking termination for revoking access**: Terminate only stops processes while preserving disks; sending a message spins it back up. **To completely revoke access, unassign the user in the IdP or remove them via Manage Group Access**.
9. **Losing secrets across multiple teams**: Joining more than two teams configured with Team Setup will result in **rejection of any Team Secrets**; simply leave the extra teams.
10. **Pinned versions dropping below minimum support threshold**: Versions locked via `apt-mark hold` that fall below the lifecycle minimum threshold will be blocked by an "Update required" screen; simply unlock and upgrade.

## Acceptance and Verification

### Network and Gateways
- Run `curl -v https://api2.cursor.sh |& grep -C1 issuer:` on office computers to ensure the certificate issuer is **Amazon RSA**.
- Run `nslookup test.us9.cursorvm.com` to test multi-level domain resolution; switch to a mobile hotspot to connect to the cloud computer and verify there are **no certificate warnings**.

### Identity and SSO
- Test logging into Grok Bot with a non-engineering account to confirm Cursor SSO succeeds on the first attempt.
- Log into internal SSO within the Bot browser using password + mobile verification code, confirming **no FastPass blocking popups**, while compliance policies on office machines remain in effect as usual.

### Private Network and Environment Scripts
- Confirm in the Tailscale or Cloudflare console that new machines join the network automatically with correct tags.
- Ping or curl private hosts in the terminal to verify connectivity; verify Team Setup logs have no timeouts and **secrets are masked**.

### Client and Security Baselines
- Silently install on Windows using a standard user account to `%LOCALAPPDATA%\Programs` and verify desktop shortcuts are generated.
- Global rules in "Settings > General > Auto-review" are locked and cannot be modified; test deleting root directory files or invoking unauthorized webhooks to confirm the system **strictly pops up an approval prompt**.

### Computer Lifecycle
- Admins execute **Recreate VMs** in the console and confirm original files and history remain intact.
- Click **Done** after batch tasks finish to verify the system can normally start the next round.

## Further Reading

- Official Documentation: [Grok Bot for Teams and Enterprise](https://cursor.com/cn/docs/grok-bot/teams)
- Official Documentation: [Configure Identity and Access](https://cursor.com/cn/docs/grok-bot/identity)
- Official Documentation: [Connect to Private Networks](https://cursor.com/cn/docs/grok-bot/private-networks)
- Official Documentation: [Configure TLS Inspection Proxies](https://cursor.com/cn/docs/grok-bot/proxies)
- Official Documentation: [Deploy Grok Bot to Your Organization](https://cursor.com/cn/docs/grok-bot/deployment)
- Official Documentation: [Manage Grok Bot Computers](https://cursor.com/cn/docs/grok-bot/computers)
- Official Help: [Plans and Billing](https://cursor.com/cn/help/grok-bot/plans)
- Official Help: [Team Bots](https://cursor.com/cn/help/grok-bot/shared-bots.md)
- Official Help: [Connect Apps](https://cursor.com/cn/help/grok-bot/connect-apps.md)
- Official Guide: [Grok Bot Security Architecture Guide](https://cursor.com/cn/docs/grok-bot/security)
