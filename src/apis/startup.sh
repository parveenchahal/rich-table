echo "Fetching access token for keyvault..."
identity_url="http://aad-identity-service.default:2424/$AAD_IDENTITY_TENANT?client_id=$AAD_IDENTITY_CLIENTID&secret=$AAD_IDENTITY_SECRET"
identity_url="$identity_url&resource=https://vault.azure.net"
accesstoken=$(curl -sS $identity_url | jq -r '.access_token')

secret_name="richtable-sql-connection-params"
echo "Fetching secret $secret_name from keyvault..."
connection_params=$(curl -sS "https://pckv1.vault.azure.net/secrets/$secret_name?api-version=2016-10-01" -H "Authorization: Bearer $accesstoken" | jq -r '.value')
export RICHTABLE_SQL_CONNECTION_PARAMS="$connection_params"

python api.py
