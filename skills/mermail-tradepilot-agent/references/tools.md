# MCP Tools Reference

## mermail_fetch_inbox

**Purpose**: Fetch pending emails from agent inbox

**Arguments**:
```json
{
  "since": "15m",  // Fetch emails from last 15 minutes
  "limit": 50      // Max emails to return
}
```

**Returns**: Array of email objects with `id`, `sender`, `subject`, `body`, `thread_id`

---

## mermail_send_email

**Purpose**: Send trade confirmation emails

**Arguments**:
```json
{
  "to": "tradepilot@mermail.app",
  "subject": "✅ Executed: BUY SOL @ $141.50",
  "body": "Transaction: 0xabc123...\nPrice: $141.50\nSize: 50 USDC"
}
```

---

## get_paybox_connection

**Purpose**: Verify PayBox connection status

**Returns**: 
- `ACTIVE` — Wallet connected, tools available
- `connect_handoff` — User must complete OAuth in browser
- `PAYBOX_UNAVAILABLE` — Not connected or owner action required

**Note**: Must call this before `tools/list` — PayBox tools may not appear in list even when available. [56]

---

## paybox_list_balances

**Purpose**: Check USDC and token balances in delegated wallets

**Returns**:
```json
{
  "USDC": "250.00",
  "SOL": "1.5",
  "wallet_address": "9xQeWvG8..."
}
```

---

## paybox_request_transfer

**Purpose**: Execute token swap or transfer

**Arguments**:
```json
{
  "token": "SOL",
  "amount_usdc": 50,
  "action": "buy",
  "slippage_bps": 50  // 0.5% slippage tolerance
}
```

**Returns**:
```json
{
  "tx_hash": "5xKjP9...",
  "status": "confirmed",
  "received_amount": "0.352 SOL"
}
```

**Security**: Requires full-profile OAuth. Workspace members can use through owner's active connection. [28][56]

---

## mermail_label_thread

**Purpose**: Organize email threads by status

**Arguments**:
```json
{
  "thread_id": "thread_abc123",
  "label": "executed"  // or "skipped", "error"
}
```