# notion-calendar

## Requirements
### Notion side
- create an integration at https://www.notion.so/my-integrations
- note down the token
- get database_id (copy link of and note down the first 32 alphanumeric string, after / and before ?)
- go on the page and share it with the integration you earlier created (top right ...-Menu)

### Azure side
- create an app registration
- note down client id and tenant id
- create a secret
- note down secret
- set redirect url to "https://login.microsoftonline.com/common/oauth2/nativeclient"

^Lets go!

## .env - File

```bash
NOTION_API_BASE=https://api.notion.com/v1
NOTION_TOKEN=
NOTION_DATABASE_ID=

TENANT_ID=
CLIENT_ID=
SECRET_ID=
```

## Run

```
python3 src/main.py
```