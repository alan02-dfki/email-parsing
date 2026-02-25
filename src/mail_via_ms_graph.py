import asyncio
from os import environ

from azure.identity import DeviceCodeCredential
from dotenv import load_dotenv
from kiota_abstractions.base_request_configuration import RequestConfiguration
from msgraph import GraphServiceClient
from msgraph.generated.users.item.messages.messages_request_builder import (
    MessagesRequestBuilder,
)


from . import CONFIG

if __name__ == "__main__":

    load_dotenv()
    emcon = CONFIG["email"]

    credentails = DeviceCodeCredential(
        # emcon["tenant_id"],
        # emcon["client_id"],
        # environ[emcon["client_secret_env_var"]],
    )

    client = GraphServiceClient(credentials=credentails, scopes=emcon["scopes"])

    async def me():
        query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
            select=["sender", "subject"],
        )

        request_configuration = RequestConfiguration(
            query_parameters=query_params,
        )

        result = await client.me.messages.get(
            request_configuration=request_configuration
        )
        print(result)
        return result

    asyncio.run(me())
