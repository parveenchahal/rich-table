identity="31ff946c-1be9-492f-92ca-c6c3119f5b21"
imdsurl="http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net&client_id=$identity"
echo "Fetching access token for keyvault..."
accesstoken=$(curl -sS "$imdsurl" -H Metadata:true | jq -r '.access_token')
secret="richtable-sql-pass"
export RICHTABLE_SQL_PASS=$(curl -sS "https://pckv1.vault.azure.net/secrets/richtable-sql-pass?api-version=2016-10-01" -H "Authorization: Bearer $accesstoken" | jq -r '.value' | base64 -d )
python api.py
