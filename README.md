# Kengine Github Action

[![GitHub License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/khulnasoft-lab/github-action/master/LICENSE) [![Github Action Community](https://img.shields.io/badge/community-Github%20Actions%20Discuss-343434.svg)](https://github.community/c/github-ecosystem/github-apps/64)

Use Github Action to run jobs on ephemeral environments automatically deployed by Kengine, authenticating into them via a bypass token.
This job connects with Kengine during a Github Action job, fetching necessary environment variables in order to run e2e tests where authentication via OAuth is normally required.

## How to use

In your Github Workflow file located in `.github/workflows/`, you can use the Kengine's Github Action as per the following example:

```
on: [pull_request]

jobs:
  cypress-e2e-tests:
    runs-on: ubuntu-latest
    name: Collect the bypass token and URL for an authenticated ephemeral environment attached to this PR in order to run e2e tests on it.
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Fetch Kengine Tokens
        uses: khulnasoft-lab/github-action/fetch-kengine-env@1.0.0
        env:
          KENGINE_API_TOKEN: ${{ secrets.KENGINE_API_TOKEN }}
      - name: Run the e2e tests on the ephemeral environment
        run: npm run test
        shell: bash
        env:
            CYPRESS_BASE_URL: $KENGINE_ENVIRONMENT_URL
            CYPRESS_BYPASS_TOKEN: $KENGINE_BYPASS_TOKEN
        
```

The Github Action can be configured by passing inputs or environment variables:

**Inputs**
```
  - name: Fetch Kengine Tokens
    uses: khulnasoft-lab/github-action/fetch-kengine-env@1.0.0
    with:
        api-token: ${{ secrets.KENGINE_API_TOKEN }}
        timeout-minutes: 30
```

| Input name | Description | Default Value |
| --------------- | --------------- |--------------- |
| `api-token` | Token required to connect to Kengine's APIs. Can be obtained from your Organization's setting page | -|
| `timeout-minutes` | Number of minutes to wait for Kengine environment before timing out. | 60|
| `app-name` | Filter the environments by name of the application on the Kengine app. | -|


**Environment Variables**
```
  - name: Fetch Kengine Tokens
    uses: khulnasoft-lab/github-action/fetch-kengine-env@1.0.0
    env:
      KENGINE_API_TOKEN: ${{ secrets.KENGINE_API_TOKEN }}
      KENGINE_TIMEOUT: 30
      INPUT_APP_NAME: 'react-app'
```

| Environment Variable | Description | Default Value |
| --------------- | --------------- |--------------- |
| `KENGINE_API_TOKEN` | Token required to connect to Kengine's APIs. Can be obtained from your Organization's setting page  |-|
| `KENGINE_TIMEOUT` | Number of minutes to wait for Kengine environment before timing out. |60|
| `KENGINE_APP_NAME` | Filter the environments by name of the application on the Kengine app. |-|

**NOTE**: Inputs are given precedence over environment variables.

If input `api-token` or environment variable `KENGINE_API_TOKEN` is not provided, error is raised.

On successful run, the following environment variables are set, which can then be passed on to other actions in the same workflow.

| Parameter Name | Description |
| --------------- | --------------- |
|`KENGINE_ENVIRONMENT_URL` | URL of the ephemeral environment |
|`KENGINE_ENVIRONMENT_ID`  | ID of the ephemeral environment  |
|`KENGINE_BYPASS_TOKEN`    | Token to bypass authentication   |


## Resources

[Kengine Documentation](https://docs.kengine.khulnasoft.com/docs/)