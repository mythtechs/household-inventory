# household-inventory
# Household Inventory Tracker

Simple, self-hosted web app to track household items (toilet paper, toothpaste, etc.).

- Add / edit / delete items
- Edit item names
- Increment / decrement / set exact quantity
- Data persists forever
- Works on Windows, Linux, macOS, Raspberry Pi

## One-command deployment

```bash
curl -O https://raw.githubusercontent.com/mythtechs/household-inventory/main/compose.yaml
docker compose up -d
