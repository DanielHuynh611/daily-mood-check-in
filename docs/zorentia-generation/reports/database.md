# Database verification

SQL assembly concatenates the approved feature SQL into `database/schema.sql`. Generation checks table coverage and SQL structure; it does not execute the schema against MySQL. Constraints, migrations and queries have not been proven by these checks.

```json
{
  "records": [
    {
      "session_id": "aafe1f4b-70cf-4a2b-bed5-cd974eacef9c",
      "source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "state": "completed",
      "manifest_hash": "3acbe8a4131336fb453e6d4f9cc8684eeefca88cf01b224d19d474e5a07db130"
    }
  ]
}
```

## Current SQL revisions

```json
{
  "records": [
    {
      "feature_id": "capability_local_data_storage_a8c07941",
      "state": "approved",
      "revision": 1,
      "last_run_id": "ec62adff-7bb8-44b1-ad4c-5a0c479fc688",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_responsive_single_column_layout_cff0cabc",
      "state": "approved",
      "revision": 1,
      "last_run_id": "023c1448-d9c9-4739-852c-aa8c6c45fbb5",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_no_sign_up_required_1ded275f",
      "state": "approved",
      "revision": 1,
      "last_run_id": "722c8fb9-0433-4097-8b30-f7b5ad98d230",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_direct_to_check_in_screen_aad4329d",
      "state": "approved",
      "revision": 1,
      "last_run_id": "b104a632-0cfc-4fa8-9df6-9d6a72065a36",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_save_mood_entry_d1f7c695",
      "state": "approved",
      "revision": 1,
      "last_run_id": "95dd318f-0ff2-4f8d-8352-c71a4edefc48",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_optional_mood_note_f6774e1f",
      "state": "approved",
      "revision": 1,
      "last_run_id": "7b317a96-4867-4180-80ee-19044a8eed24",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_five_mood_options_selection_fb56ebd0",
      "state": "approved",
      "revision": 1,
      "last_run_id": "aa0271bc-f3d9-451d-b7f6-ba94564b7035",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_chronological_history_view_14184bae",
      "state": "approved",
      "revision": 1,
      "last_run_id": "7a39112b-597f-41f2-819a-9fde7e586378",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_save_confirmation_message_41f550eb",
      "state": "approved",
      "revision": 1,
      "last_run_id": "43cede7f-3295-4eca-a9bb-b40a7869e5c4",
      "last_error_code": null,
      "last_error_details": null
    }
  ]
}
```

## Run history
Compare each feature's last_run_id with these run IDs. Failed/superseded runs are historical; compare source hashes.

```json
{
  "records": [
    {
      "id": "ec62adff-7bb8-44b1-ad4c-5a0c479fc688",
      "scope_key": "feature:capability_local_data_storage_a8c07941",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:04",
      "finished_at": "2026-09-30 09:39:06",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2213,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "023c1448-d9c9-4739-852c-aa8c6c45fbb5",
      "scope_key": "feature:capability_responsive_single_column_layout_cff0cabc",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:37",
      "finished_at": "2026-09-30 09:39:37",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "722c8fb9-0433-4097-8b30-f7b5ad98d230",
      "scope_key": "feature:capability_no_sign_up_required_1ded275f",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:43",
      "finished_at": "2026-09-30 09:39:43",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "b104a632-0cfc-4fa8-9df6-9d6a72065a36",
      "scope_key": "feature:capability_direct_to_check_in_screen_aad4329d",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:47",
      "finished_at": "2026-09-30 09:39:48",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "95dd318f-0ff2-4f8d-8352-c71a4edefc48",
      "scope_key": "feature:capability_save_mood_entry_d1f7c695",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:51",
      "finished_at": "2026-09-30 09:39:53",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 1819,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "7b317a96-4867-4180-80ee-19044a8eed24",
      "scope_key": "feature:capability_optional_mood_note_f6774e1f",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:39:57",
      "finished_at": "2026-09-30 09:39:58",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 1254,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "aa0271bc-f3d9-451d-b7f6-ba94564b7035",
      "scope_key": "feature:capability_five_mood_options_selection_fb56ebd0",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:40:03",
      "finished_at": "2026-09-30 09:40:05",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 1441,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "7a39112b-597f-41f2-819a-9fde7e586378",
      "scope_key": "feature:capability_chronological_history_view_14184bae",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:40:10",
      "finished_at": "2026-09-30 09:40:11",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 1490,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "43cede7f-3295-4eca-a9bb-b40a7869e5c4",
      "scope_key": "feature:capability_save_confirmation_message_41f550eb",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
      "created_at": "2026-09-30 09:40:26",
      "finished_at": "2026-09-30 09:40:26",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    }
  ]
}
```


For a recorded table/SQL error, inspect the identified table in `database/schema.sql` and the run details. Apply the schema to a local MySQL database following the README to obtain actual database execution results. If no cause or location was captured, it is unknown; missing history is not a pass.
