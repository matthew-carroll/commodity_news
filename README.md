# Commodity News
AI generated news about commodity prices.

## Gold Price APIs
We use two APIs for gold prices. They're interchangeable. We use two so that we get twice the request count.

https://metalpriceapi.com/documentation

https://www.goldapi.io/

### API Keys
Both services require API keys for access. The API keys are free.

Store the API keys in environment variables with the following names:

 * METALPRICE_API_KEY
 * GOLDAPIIO_API_KEY

### TODOs
* Maintain more detailed context across summarizations so output script is less abstract and more concrete/specific.
