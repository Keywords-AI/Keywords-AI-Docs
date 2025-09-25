# Log Scores Management API

The Log Scores Management API allows you to create, retrieve, update, and delete evaluation scores for specific logs. This ensures that only one score exists per evaluator per log, providing clean score management for your logged requests.

## Overview

The scoring system ensures uniqueness by enforcing that each evaluator (identified by either `evaluator_id` or `evaluator_slug`) can only have one score per log. This prevents duplicate scores and maintains data integrity.

### Key Concepts

- **Log ID**: The unique identifier of the request log you want to score
- **Score ID**: The unique identifier of a specific score (returned as `id` in responses)
- **Evaluator ID**: The UUID of an evaluator created in Keywords AI platform (managed evaluators)
- **Evaluator Slug**: A custom string identifier that you define for your own custom evaluators

## Authentication

All endpoints require authentication via either:

- JWT token: `Authorization: Bearer <token>`
- API key: `Authorization: Bearer <key>`

## Endpoints
## Score Fields and Evaluator Rules

Scores support four value fields. Set the field that matches the evaluator's `score_value_type`:

- numerical_value (number): Use when the evaluator's `score_value_type` is `numerical`
- boolean_value (boolean): Use when the evaluator's `score_value_type` is `boolean`
- categorical_value (array of strings): Use when the evaluator's `score_value_type` is `categorical`
- string_value (string): Use when the evaluator's `score_value_type` is `comment`

See the Evaluators API for details on `score_value_type` and configuring categorical choices (refer to `evaluators_api_docs.md`).


### 1. Create a Score

Creates a new evaluation score for a specific log.

**Endpoint:** `POST /api/logs/{log_id}/scores/`

#### Request Body

You must provide either `evaluator_id` (for evaluators created in Keywords AI platform) or `evaluator_slug` (a custom string for your own evaluators), plus at least one score value.

```json
{
  "evaluator_id": "uuid-of-keywordsai-evaluator", // Optional: UUID of evaluator created in Keywords AI
  "evaluator_slug": "my_custom_evaluator", // Optional: Custom string identifier for your evaluator
  "numerical_value": 4.5, // Optional: Numerical score
  "string_value": "Good response quality", // Optional: String score
  "boolean_value": true, // Optional: Boolean score
  "categorical_value": ["excellent", "coherent"] // Optional: Categorical score (list of strings)
}
```

#### Response (201 Created)

```json
{
  "id": "eval_result_unique_id",
  "created_at": "2024-01-15T10:30:00Z",
  "type": "llm",
  "environment": "test",
  "numerical_value": 4.5,
  "string_value": "Good response quality",
  "boolean_value": true,
  "categorical_value": ["excellent"],
  "is_passed": false,
  "cost": 0.0,
  "evaluator_id": null,
  "evaluator_slug": "my_custom_evaluator",
  "log_id": null,
  "dataset_id": null
}
```

#### Error Responses

**409 Conflict** - Score already exists for this evaluator in this log:

```json
{
  "error": "A score already exists for this evaluator in this log."
}
```

**400 Bad Request** - Invalid request data:

```json
{
  "error": "Either evaluator_id or evaluator_slug must be provided"
}
```

### 2. List Scores for a Log

Retrieves all scores associated with a specific log.

**Endpoint:** `GET /api/logs/{log_id}/scores/`

#### Response (200 OK)

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "eval_result_unique_id_1",
      "created_at": "2024-01-15T10:30:00Z",
      "type": "llm",
      "environment": "test",
      "numerical_value": 4.5,
      "string_value": "Good quality",
      "boolean_value": true,
      "categorical_value": ["excellent"],
      "is_passed": false,
      "cost": 0.0,
      "evaluator_id": null,
      "evaluator_slug": "quality_evaluator",
      "log_id": "log_unique_id",
      "dataset_id": null
    },
    {
      "id": "eval_result_unique_id_2",
      "created_at": "2024-01-15T10:32:00Z",
      "type": "llm",
      "environment": "test",
      "numerical_value": 3.8,
      "string_value": "Mostly relevant",
      "boolean_value": true,
      "categorical_value": ["relevant"],
      "is_passed": false,
      "cost": 0.0,
      "evaluator_id": null,
      "evaluator_slug": "relevance_evaluator",
      "log_id": "log_unique_id",
      "dataset_id": null
    }
  ]
}
```

### 3. Retrieve a Specific Score (Log-scoped)

Gets detailed information about a specific score.

**Endpoint:** `GET /api/logs/{log_id}/scores/{score_id}/`

#### Response (200 OK)

```json
{
  "id": "eval_result_unique_id",
  "created_at": "2024-01-15T10:30:00Z",
  "type": "llm",
  "environment": "test",
  "numerical_value": 4.5,
  "string_value": "Good quality",
  "boolean_value": true,
  "categorical_value": ["excellent"],
  "is_passed": false,
  "cost": 0.0,
  "evaluator_id": null,
  "evaluator_slug": "quality_evaluator",
  "log_id": "log_unique_id",
  "dataset_id": null
}
```

### 4. Update a Score

Updates an existing score. You can update any combination of score values.

**Endpoint:** `PATCH /api/logs/{log_id}/scores/{score_id}/`

#### Request Body

```json
{
  "numerical_value": 4.8, // Optional: Updated numerical score
  "string_value": "Excellent quality", // Optional: Updated string score
  "boolean_value": true, // Optional: Updated boolean score
  "categorical_value": ["excellent", "accurate"] // Optional: Updated categorical score
}
```

#### Response (200 OK)

```json
{
  "id": "eval_result_unique_id",
  "created_at": "2024-01-15T10:30:00Z",
  "type": "llm",
  "environment": "test",
  "numerical_value": 4.8,
  "string_value": "Excellent quality",
  "boolean_value": true,
  "categorical_value": ["excellent", "accurate"],
  "is_passed": false,
  "cost": 0.0,
  "evaluator_id": null,
  "evaluator_slug": "quality_evaluator",
  "log_id": "log_unique_id",
  "dataset_id": null
}
```

### 5. Delete a Score

Removes a score from a log.

**Endpoint:** `DELETE /api/logs/{log_id}/scores/{score_id}/`

#### Response (204 No Content)

No response body is returned for successful deletions.

## Usage Examples

### Creating a Score with Custom Evaluator

```bash
curl -X POST "https://api.keywordsai.co/api/logs/my-log-id/scores/" \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "evaluator_slug": "response_quality",
    "numerical_value": 4.2,
    "string_value": "Good response with minor issues",
    "boolean_value": true,
    "categorical_value": ["coherent", "helpful"]
  }'
```

**Note**: The `evaluator_slug` can be any custom string you choose to identify your evaluator (e.g., "quality_check", "relevance_score", "custom_eval_v1").

### Creating a Score with Keywords AI Evaluator

```bash
curl -X POST "https://api.keywordsai.co/api/logs/my-log-id/scores/" \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "evaluator_id": "550e8400-e29b-41d4-a716-446655440000",
    "numerical_value": 3.8
  }'
```

**Note**: The `evaluator_id` must be a evaluator ID copied from the Keywords AI platform.

### Listing All Scores for a Log

```bash
curl -X GET "https://api.keywordsai.co/api/logs/my-log-id/scores/" \
  -H "Authorization: Bearer <your-jwt-token>"
```

### Updating a Score

```bash
curl -X PATCH "https://api.keywordsai.co/api/logs/my-log-id/scores/score-unique-id/" \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "numerical_value": 4.5,
    "string_value": "Updated assessment"
  }'
```

### Deleting a Score

```bash
curl -X DELETE "https://api.keywordsai.co/api/logs/my-log-id/scores/score-unique-id/" \
  -H "Authorization: Bearer <your-jwt-token>"
```

## Log Enrichment

When you retrieve log details, scores are automatically included in the response under a `scores` field:

```json
{
  "id": "my-log-id",
  "model": "gpt-4",
  "prompt_tokens": 150,
  "completion_tokens": 75,
  "scores": {
    "response_quality": {
      "evaluator_slug": "response_quality",
      "numerical_value": 4.2,
      "string_value": "Good response",
      "boolean_value": true,
      "categorical_value": ["coherent"],
      "is_passed": false,
      "cost": 0.0
    },
    "relevance_check": {
      "evaluator_slug": "relevance_check",
      "numerical_value": 3.8,
      "string_value": "Mostly relevant",
      "boolean_value": true,
      "categorical_value": ["relevant"],
      "is_passed": false,
      "cost": 0.0
    }
  }
}
```

## Best Practices

1. **Use descriptive evaluator slugs** - Make them meaningful and consistent across your application
2. **Handle uniqueness errors** - Always check for 409 Conflict responses when creating scores
3. **Validate score types** - Ensure you're using the appropriate score type (numerical, string, boolean, categorical) for your use case
4. **Batch operations carefully** - Since these are manual operations (max ~50 calls/sec), avoid overwhelming the API
5. **Store score IDs** - Keep track of score IDs if you need to update or delete them later

## Error Handling

The API returns standard HTTP status codes:

- `200 OK` - Successful GET/PATCH requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Invalid or missing authentication
- `404 Not Found` - Log or score not found
- `409 Conflict` - Score already exists for this evaluator in this log

Always check the response status code and handle errors appropriately in your application.


## Unified Inputs on Scores

Each score (EvalResult) may store the unified evaluator inputs in its `inputs` attribute. This follows the same unified format described in the Evaluators API docs.

Shape:

```json
{
  "inputs": {
    "input": {},
    "output": {},
    "metrics": {},
    "metadata": {}
  }
}
```

- `input` (any JSON): The request/input that was evaluated
- `output` (any JSON): The response/output that was evaluated
- `metrics` (object, optional): System-captured metrics (tokens, latency, cost)
- `metadata` (object, optional): Context and custom properties you passed

Notes:

- Legacy fields (`llm_input`, `llm_output`) are normalized to `input`/`output` when reading the `inputs` field from a score.
- The unified `inputs` object is included in the EvalResult detail response where available. See Evaluators API for more on the unified inputs format (refer to `evaluators/evaluators_api_docs.md`).

## Metrics and Metadata Fields

When present, `inputs.metrics` and `inputs.metadata` include the following:

- Metrics
  - start_time: Request start time (RFC3339)
  - timestamp: Span end time (RFC3339)
  - prompt_tokens: Tokens in the prompt/input
  - completion_tokens: Tokens in the model output
  - prompt_cache_hit_tokens: Tokens served from cache
  - prompt_cache_creation_tokens: Tokens added to cache
  - total_request_tokens: Sum of prompt and completion tokens
  - latency: Total request latency in seconds
  - time_to_first_token: Time from request start to first output token
  - tokens_per_second: Output token throughput (TPS)
  - routing_time: Deprecated; time spent deciding the model/route
  - cost: Total request cost (USD)

- Metadata
  - unique_id: Request unique identifier
  - unique_organization_id: Organization unique identifier
  - organization_key_id: API key identifier
  - environment: Runtime environment (e.g., test, prod)
  - customer_identifier: User/customer-level identifier
  - evaluation_identifier: Evaluator run identifier
  - prompt_id: Prompt identifier
  - prompt_version_number: Prompt version
  - custom_identifier: Custom identifier provided by client
  - thread_identifier: Logical thread id
  - thread_unique_id: Unique id of thread
  - trace_unique_id: Trace id
  - span_unique_id: Span id
  - span_name: Span name
  - span_parent_id: Parent span id
  - span_workflow_name: Workflow name
  - trace_group_identifier: Trace group id
  - deployment_name: Deployment name
  - provider_id: Provider identifier
  - model: Model name
  - status_code: HTTP-like status code
  - status: Status string
  - tool_calls: Tool calls recorded
  - LLM configuration fields: stream, stream_options, temperature, max_tokens, logit_bias, logprobs, top_logprobs, frequency_penalty, presence_penalty, stop, n, response_format, verbosity, tools

Notes:

- Some fields may be omitted depending on provider/model and request path.
- `routing_time` is deprecated and retained for historical compatibility.

## Global Score Management

The global Scores API allows listing and retrieving scores without scoping to a specific log.

### 1. List Scores

Lists scores for your organization with filtering and pagination support.

**Endpoint:** `GET /api/scores/list/`

#### Response (200 OK)

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "score_unique_id",
      "created_at": "2025-09-16T10:19:10.261066Z",
      "type": "llm",
      "environment": "test",
      "numerical_value": 1,
      "string_value": null,
      "boolean_value": null,
      "categorical_value": [],
      "is_passed": false,
      "cost": 0.00002625,
      "evaluator_id": "93c77977-c414-4a06-8f97-292eda6ad31c",
      "evaluator_slug": "response_quality_v1",
      "log_id": null,
      "dataset_id": null
    }
  ]
}
```

### 2. Retrieve Score Details

Retrieves a score by its ID. Returns the `evaluator` and `inputs` objects in addition to the core fields.

**Endpoint:** `GET /api/scores/{score_id}/`

#### Response (200 OK)

```json
{
  "id": "score_unique_id",
  "created_at": "2025-09-16T10:19:10.261066Z",
  "type": "llm",
  "environment": "test",
  "numerical_value": 1,
  "string_value": null,
  "boolean_value": null,
  "categorical_value": [],
  "is_passed": false,
  "cost": 0.00002625,
  "evaluator_id": "93c77977-c414-4a06-8f97-292eda6ad31c",
  "evaluator_slug": "response_quality_v1",
  "log_id": null,
  "dataset_id": null,
  "evaluator": {
    "id": "93c77977-c414-4a06-8f97-292eda6ad31c",
    "configurations": {
      "llm_engine": "gpt-4o-mini",
      "model_options": {
        "model": "gpt-4o",
        "top_p": 1,
        "max_tokens": 200,
        "temperature": 0.1,
        "presence_penalty": 0,
        "reasoning_effort": "low",
        "frequency_penalty": 0
      },
      "evaluator_definition": "Rate the response quality based on accuracy, relevance, and completeness. <llm_input>{{llm_input}}</llm_input><llm_output>{{llm_output}}</llm_output>",
      "scoring_rubric": "1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
      "min_score": 1,
      "max_score": 5,
      "passing_score": 3
    },
    "categorical_choices": [],
    "eval_class": "keywordsai_custom_llm",
    "created_by": {
      "first_name": "Keywords AI",
      "last_name": "Team",
      "email": "admin@keywordsai.co"
    },
    "updated_by": {
      "first_name": "Keywords AI",
      "last_name": "Team",
      "email": "admin@keywordsai.co"
    },
    "evaluator_slug": "response_quality_v1",
    "name": "Response Quality Evaluator",
    "description": "Evaluates response quality on a 1-5 scale",
    "created_at": "2025-09-13T23:38:50.549222Z",
    "updated_at": "2025-09-14T05:04:52.101379Z",
    "type": "llm",
    "score_value_type": "numerical",
    "custom_required_fields": ["llm_input", "llm_output"],
    "starred": false,
    "tags": []
  },
  "inputs": {
    "input": "...",
    "output": "...",
    "metrics": null,
    "metadata": null
  }
}
```

Notes:

- The `inputs` object follows the unified format documented above and in the Evaluators API docs.
- Only list and retrieve are documented here to avoid confusion; use Log Scores Management for creating/updating/deleting scores.