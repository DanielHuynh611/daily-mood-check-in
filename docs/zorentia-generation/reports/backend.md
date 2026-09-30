# Backend verification

Static checks inspect Python syntax, internal import paths, declared routes/functions, file integrity and credential patterns. `database_contract` means the schema file exists; `dependency_resolution` means requirements.txt exists, not that installation succeeded. `file_integrity` is the verifier's aggregate static result. The raw evidence identifies individual errors. The checked-input package hash below covers the files before reports were added.

## Findings and next steps

```json
{
  "finding": "assembled_duplicate_route:GET:/health"
}
```

Expected the declared functions and routes to be present without conflicting registrations. Compare the reported identifier/method/path with the feature handler and route map.

## Check evidence and coverage
```json
{
  "schema_version": "assembled-backend-verification",
  "source": {
    "architecture_session_id": "da0786ca-5499-468c-9529-7055a04f4b27",
    "architecture_id": "architecture:scope_daily_80dbef67:cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71",
    "architecture_source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71"
  },
  "package_hash": "5e2c4cfa32d67a298e4c25eb62a3efb552d7e4b6501aef4032e28d56ecb8ff85",
  "static_valid": false,
  "passes": {
    "file_integrity": false,
    "imports": true,
    "route_map": false,
    "function_coverage": true,
    "database_contract": true,
    "dependency_resolution": true,
    "secret_scan": "[redacted]"
  },
  "features": {
    "covered": 9,
    "total": 9
  },
  "functions": {
    "covered": 10,
    "total": 10
  },
  "errors": [
    "assembled_duplicate_route:GET:/health"
  ],
  "warnings": [],
  "report_hash": "850d898cb7d1ba0ad010dade6dabcde1e02227e04c054042550fa5814f81ecf7",
  "not_run": [
    "database execution",
    "dependency installation",
    "application startup",
    "pytest",
    "integration tests",
    "business behavior"
  ]
}
```

## Feature sources
```json
[
  {
    "feature_id": "capability_local_data_storage_a8c07941",
    "state": "complete",
    "architecture_backend_hash": "21d87e2c9d4d891d45a7a463726815ec773ff1baf8f866654372deba4f441a80",
    "database_feature_sql_hash": "137a4d98966bba7ceb97c013233c18535a81b4a91ef9459747c2e2d1dfb2c6fb",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_responsive_single_column_layout_cff0cabc",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "6dd6e20e2867388d640f7d4b89ef2df430bfd24e580e93c723b8d19aa5514c39",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_no_sign_up_required_1ded275f",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "00bab5109a2bad06517dd065d7f7f5fd3440fe8cd8de7700c185af713b7ba096",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_direct_to_check_in_screen_aad4329d",
    "state": "complete",
    "architecture_backend_hash": "87d19e7e1617e6d9fb50a8b93cd18338ec24303b85ec8bbbfadb8a3a1bcffc5a",
    "database_feature_sql_hash": "97bfc2458a17d621a7e572347fa2b4fd71bf558ccd099336ac66e1833fa12a20",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_save_mood_entry_d1f7c695",
    "state": "complete",
    "architecture_backend_hash": "3ec70d1e3c6e2f353b0087b745337cc4ce026e4cbe93c8d1a7c33036480e9144",
    "database_feature_sql_hash": "e32bae1f82806bd0e5709afcc8fe0694ba960a798b02cd7438502ee429b57a77",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_optional_mood_note_f6774e1f",
    "state": "complete",
    "architecture_backend_hash": "a93ce003df8b4a5b8094b0463238a46a3074434592813ee0784ce2df7c1fcf30",
    "database_feature_sql_hash": "24b518b5c5126a8d925b414d9cc09ed6aa80facf0634d47a01a9df72fd5ed275",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_five_mood_options_selection_fb56ebd0",
    "state": "complete",
    "architecture_backend_hash": "dedbb2a36bc6be48639accfaa0e85117092dd7a1e03586dfed258f6f35064ee0",
    "database_feature_sql_hash": "e935142d0f514b246316a41f847ccd92c2f1de05ef2b8330b7251eae0428070a",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_chronological_history_view_14184bae",
    "state": "complete",
    "architecture_backend_hash": "846e6e9c88d8e31a7cce228afb4faa8e64be22e26332b4d078817512460aa28c",
    "database_feature_sql_hash": "7ee8d14c3db59622ae6d3084f54c4337ed9d3b5a40ac919d73b15f649b8b2e5a",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_save_confirmation_message_41f550eb",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "c84ddb59e366f024878fce9a82785d9b1eab80bb60641b541f92c0aec2df8d3a",
    "last_error_code": null,
    "last_error_details": []
  }
]
```

## Expected feature routes and functions
```json
[
  {
    "feature_id": "capability_local_data_storage_a8c07941",
    "functions": [
      {
        "id": "capability_local_data_storage_a8c07941.function.create_mood_entry",
        "name": "create_mood_entry",
        "http_method": "POST",
        "route": "/api/capability_local_data_storage_a8c07941/mood-entries",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_local_data_storage_a8c07941.function.list_mood_entries",
        "name": "list_mood_entries",
        "http_method": "GET",
        "route": "/api/capability_local_data_storage_a8c07941/mood-entries",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_responsive_single_column_layout_cff0cabc",
    "functions": []
  },
  {
    "feature_id": "capability_no_sign_up_required_1ded275f",
    "functions": []
  },
  {
    "feature_id": "capability_direct_to_check_in_screen_aad4329d",
    "functions": [
      {
        "id": "capability_direct_to_check_in_screen_aad4329d.function.get_today_date",
        "name": "get_today_date",
        "http_method": "GET",
        "route": "/api/capability_direct_to_check_in_screen_aad4329d/today",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_save_mood_entry_d1f7c695",
    "functions": [
      {
        "id": "capability_save_mood_entry_d1f7c695.function.create_mood_entry",
        "name": "create_mood_entry",
        "http_method": "POST",
        "route": "/api/capability_save_mood_entry_d1f7c695/mood-entries",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_optional_mood_note_f6774e1f",
    "functions": [
      {
        "id": "capability_optional_mood_note_f6774e1f.function.create_mood_entry",
        "name": "create_mood_entry",
        "http_method": "POST",
        "route": "/api/capability_optional_mood_note_f6774e1f/mood-entries",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_optional_mood_note_f6774e1f.function.get_mood_entries",
        "name": "get_mood_entries",
        "http_method": "GET",
        "route": "/api/capability_optional_mood_note_f6774e1f/mood-entries",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_five_mood_options_selection_fb56ebd0",
    "functions": [
      {
        "id": "capability_five_mood_options_selection_fb56ebd0.function.get_mood_options",
        "name": "get_mood_options",
        "http_method": "GET",
        "route": "/api/capability_five_mood_options_selection_fb56ebd0/mood-options",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry",
        "name": "create_mood_entry",
        "http_method": "POST",
        "route": "/api/capability_five_mood_options_selection_fb56ebd0/mood-entries",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_five_mood_options_selection_fb56ebd0.function.get_latest_mood_entry",
        "name": "get_latest_mood_entry",
        "http_method": "GET",
        "route": "/api/capability_five_mood_options_selection_fb56ebd0/mood-entries/latest",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_chronological_history_view_14184bae",
    "functions": [
      {
        "id": "capability_chronological_history_view_14184bae.function.get_mood_history",
        "name": "get_mood_history",
        "http_method": "GET",
        "route": "/api/capability_chronological_history_view_14184bae/mood-entries",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_save_confirmation_message_41f550eb",
    "functions": []
  }
]
```

## Generation and repair history

Failed attempts below are historical, not automatically defects in these files. A matching file hash identifies a checked output retained in this package. Earlier discarded evidence cannot be reconstructed. An empty history does not mean every attempt passed.

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_local_data_storage_a8c07941",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/local_data_storage/feature.py",
          "sha256": "322a7b5cdf6f2db06e11a51998610bb04667fa336f0ad6808020241162142152"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_local_data_storage_a8c07941",
        "file_count": 1,
        "function_ids": [
          "capability_local_data_storage_a8c07941.function.create_mood_entry",
          "capability_local_data_storage_a8c07941.function.list_mood_entries"
        ],
        "function_names": [
          "create_mood_entry",
          "list_mood_entries"
        ],
        "route_count": 2,
        "verification_hash": "c49932aa5b51d494dab193adbeca55afe6275450c0e8049c29d594d07fa8612c"
      }
    }
  ],
  "started_at": "2026-09-30T09:40:40.883444+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_local_data_storage_a8c07941",
  "screen_id": null,
  "expected_workspace_version": 1,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "21d87e2c9d4d891d45a7a463726815ec773ff1baf8f866654372deba4f441a80",
    "database_feature_sql_hash": "137a4d98966bba7ceb97c013233c18535a81b4a91ef9459747c2e2d1dfb2c6fb"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:40:55.496789+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_responsive_single_column_layout_cff0cabc",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/responsive_single_column_layout/feature.py",
          "sha256": "9b131009534f622b071e928cad56484f4889062155d3dbcfb0b1dfd696999f9c"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_responsive_single_column_layout_cff0cabc",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 1,
        "verification_hash": "684842cbec6215713e1324aebd2a237c7f26c8ea225dc4a61fba0e32cd5e32de"
      }
    }
  ],
  "started_at": "2026-09-30T09:41:01.893328+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_responsive_single_column_layout_cff0cabc",
  "screen_id": null,
  "expected_workspace_version": 3,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "6dd6e20e2867388d640f7d4b89ef2df430bfd24e580e93c723b8d19aa5514c39"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:41:07.538405+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_save_confirmation_message_41f550eb",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/save_confirmation_message/feature.py",
          "sha256": "5c0e1914efee00f47c80d6b4b2e13c295b51625fc4df78421285d3040f943c0d"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_save_confirmation_message_41f550eb",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 6,
        "verification_hash": "2fd1ad0b3774b9328b752d520dd2c7f227c3eb82aa1bdb711f34da2f2c9a9e04"
      }
    }
  ],
  "started_at": "2026-09-30T09:41:15.647207+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_save_confirmation_message_41f550eb",
  "screen_id": null,
  "expected_workspace_version": 5,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "c84ddb59e366f024878fce9a82785d9b1eab80bb60641b541f92c0aec2df8d3a"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:41:34.124929+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_no_sign_up_required_1ded275f",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/no_sign_up_required/feature.py",
          "sha256": "8542f1bc81eb0b356cef727b4a4899e8ec40e6a270aba4ac598bd90547d6a4ce"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_no_sign_up_required_1ded275f",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 3,
        "verification_hash": "b5a6a581825c17a18b03d3a9969fab9ecc0010fc234949fe530e3b9a9a9669f6"
      }
    }
  ],
  "started_at": "2026-09-30T09:41:59.795402+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_no_sign_up_required_1ded275f",
  "screen_id": null,
  "expected_workspace_version": 7,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "00bab5109a2bad06517dd065d7f7f5fd3440fe8cd8de7700c185af713b7ba096"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:42:20.803174+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_direct_to_check_in_screen_aad4329d",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/direct_to_check_in_screen/feature.py",
          "sha256": "ca5ff5668f11a312dc9043464a9ba0e657159902ba4d077ef96a043e1ca0a16a"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_direct_to_check_in_screen_aad4329d",
        "file_count": 1,
        "function_ids": [
          "capability_direct_to_check_in_screen_aad4329d.function.get_today_date"
        ],
        "function_names": [
          "get_today_date"
        ],
        "route_count": 1,
        "verification_hash": "f972904625e32f6ef4e42998104cda43035e55e8f55af443cc486daf4ea5afa5"
      }
    }
  ],
  "started_at": "2026-09-30T09:42:30.990832+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_direct_to_check_in_screen_aad4329d",
  "screen_id": null,
  "expected_workspace_version": 9,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "87d19e7e1617e6d9fb50a8b93cd18338ec24303b85ec8bbbfadb8a3a1bcffc5a",
    "database_feature_sql_hash": "97bfc2458a17d621a7e572347fa2b4fd71bf558ccd099336ac66e1833fa12a20"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:42:37.191006+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_save_mood_entry_d1f7c695",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/save_mood_entry/feature.py",
          "sha256": "eb28b223f47b893e4a279a4f5ca6be76336e502f82c767357079490ac5dd53f2"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_save_mood_entry_d1f7c695",
        "file_count": 1,
        "function_ids": [
          "capability_save_mood_entry_d1f7c695.function.create_mood_entry"
        ],
        "function_names": [
          "create_mood_entry"
        ],
        "route_count": 1,
        "verification_hash": "493c8f5c1b202dc9ff813c62329aaf16b138f4e2b557ef1bdb101234b852c25f"
      }
    }
  ],
  "started_at": "2026-09-30T09:42:41.860519+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_save_mood_entry_d1f7c695",
  "screen_id": null,
  "expected_workspace_version": 11,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "3ec70d1e3c6e2f353b0087b745337cc4ce026e4cbe93c8d1a7c33036480e9144",
    "database_feature_sql_hash": "e32bae1f82806bd0e5709afcc8fe0694ba960a798b02cd7438502ee429b57a77"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:42:52.833713+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_optional_mood_note_f6774e1f",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/optional_mood_note/feature.py",
          "sha256": "9ee9b8b87ba18bfa80154612f64537622aa62111e9325d4b64b2b60313a36cb3"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_optional_mood_note_f6774e1f",
        "file_count": 1,
        "function_ids": [
          "capability_optional_mood_note_f6774e1f.function.create_mood_entry",
          "capability_optional_mood_note_f6774e1f.function.get_mood_entries"
        ],
        "function_names": [
          "create_mood_entry",
          "get_mood_entries"
        ],
        "route_count": 2,
        "verification_hash": "7f1533792ae9d53f13937e370ee1ab7a213102128471d7f2df8e45f6d7be9768"
      }
    }
  ],
  "started_at": "2026-09-30T09:42:56.654908+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_optional_mood_note_f6774e1f",
  "screen_id": null,
  "expected_workspace_version": 13,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "a93ce003df8b4a5b8094b0463238a46a3074434592813ee0784ce2df7c1fcf30",
    "database_feature_sql_hash": "24b518b5c5126a8d925b414d9cc09ed6aa80facf0634d47a01a9df72fd5ed275"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:43:07.217700+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_five_mood_options_selection_fb56ebd0",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/five_mood_options_selection/feature.py",
          "sha256": "d0ea7dd4c95d1e2f8059681d1d1dd2276703b9cbda2888e31aa65ee772c5e010"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_five_mood_options_selection_fb56ebd0",
        "file_count": 1,
        "function_ids": [
          "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry",
          "capability_five_mood_options_selection_fb56ebd0.function.get_latest_mood_entry",
          "capability_five_mood_options_selection_fb56ebd0.function.get_mood_options"
        ],
        "function_names": [
          "create_mood_entry",
          "get_latest_mood_entry",
          "get_mood_options"
        ],
        "route_count": 3,
        "verification_hash": "f1085796fc390f64efd838906f87805d38a1be85c76583f1dc2ccb0f7a273a24"
      }
    }
  ],
  "started_at": "2026-09-30T09:43:12.042348+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_five_mood_options_selection_fb56ebd0",
  "screen_id": null,
  "expected_workspace_version": 15,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "dedbb2a36bc6be48639accfaa0e85117092dd7a1e03586dfed258f6f35064ee0",
    "database_feature_sql_hash": "e935142d0f514b246316a41f847ccd92c2f1de05ef2b8330b7251eae0428070a"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:43:23.757188+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_chronological_history_view_14184bae",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/chronological_history_view/feature.py",
          "sha256": "4f8cb4fa45f2e7bc68caecd5199464983d6556a4504b1afd2338c5386c188b74"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_chronological_history_view_14184bae",
        "file_count": 1,
        "function_ids": [
          "capability_chronological_history_view_14184bae.function.get_mood_history"
        ],
        "function_names": [
          "get_mood_history"
        ],
        "route_count": 1,
        "verification_hash": "bde0d932c05516b3c5542008ce489485a0ba5eba380edf0c27685c7de201bbd3"
      }
    }
  ],
  "started_at": "2026-09-30T09:43:32.907834+00:00",
  "workspace_id": "8257e579-9af0-4968-a923-621677a86e0f",
  "feature_id": "capability_chronological_history_view_14184bae",
  "screen_id": null,
  "expected_workspace_version": 17,
  "session_id": "2524c616-5eed-4d12-aab1-5233e276fb8f",
  "mvp_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
  "source": {
    "architecture_backend_hash": "846e6e9c88d8e31a7cce228afb4faa8e64be22e26332b4d078817512460aa28c",
    "database_feature_sql_hash": "7ee8d14c3db59622ae6d3084f54c4337ed9d3b5a40ac919d73b15f649b8b2e5a"
  },
  "outcome": "completed",
  "finished_at": "2026-09-30T09:43:39.342044+00:00"
}
```
