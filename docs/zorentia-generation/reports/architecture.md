# Architecture verification

These are contract and coverage checks, not executable application tests. The current blueprint evidence is below. Historical attempts may refer to an earlier scope; compare scope hashes.

## Current blueprint
```json
{
  "source": {
    "scope_id": "scope_daily_80dbef67",
    "source_session_id": "ffcc87bb-5885-49e7-865d-11e0b840efe9",
    "source_hash": "cb84b980811323959458e6c45d16c1fe809a913eae2ea3b34b9d045720d02c71"
  },
  "blueprint_hash": "0ff4aaba61c3d65966e07cdf0ee02e5220f768fc2a00d4f64e0335fbc6521d24",
  "assembly": {
    "valid": true,
    "errors": []
  },
  "coverage": {
    "valid": true,
    "features": {
      "covered": 9,
      "total": 9
    },
    "acceptance_criteria": {
      "covered": 36,
      "total": 36
    }
  },
  "features": [
    {
      "feature_id": "capability_local_data_storage_a8c07941",
      "verification": {
        "valid": true,
        "feature_id": "capability_local_data_storage_a8c07941",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_data_remains_private_to_the_current_de_d8db2fc3",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ],
            "function_ids": [
              "capability_local_data_storage_a8c07941.function.create_mood_entry",
              "capability_local_data_storage_a8c07941.function.list_mood_entries"
            ],
            "screen_ids": [
              "capability_local_data_storage_a8c07941.screen.check_in",
              "capability_local_data_storage_a8c07941.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_each_entry_includes_date_selected_mood_7ef2e01d",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ],
            "function_ids": [
              "capability_local_data_storage_a8c07941.function.create_mood_entry",
              "capability_local_data_storage_a8c07941.function.list_mood_entries"
            ],
            "screen_ids": [
              "capability_local_data_storage_a8c07941.screen.check_in",
              "capability_local_data_storage_a8c07941.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_entries_are_stored_using_browser_local_54fbd257",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ],
            "function_ids": [
              "capability_local_data_storage_a8c07941.function.create_mood_entry",
              "capability_local_data_storage_a8c07941.function.list_mood_entries"
            ],
            "screen_ids": [
              "capability_local_data_storage_a8c07941.screen.check_in",
              "capability_local_data_storage_a8c07941.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_mood_entries_persist_after_closing_and_bbb3d764",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ],
            "function_ids": [
              "capability_local_data_storage_a8c07941.function.create_mood_entry",
              "capability_local_data_storage_a8c07941.function.list_mood_entries"
            ],
            "screen_ids": [
              "capability_local_data_storage_a8c07941.screen.check_in",
              "capability_local_data_storage_a8c07941.screen.history"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_local_data_storage_a8c07941.screen.check_in",
            "action_id": "capability_local_data_storage_a8c07941.screen-action.save_mood_entry",
            "function_id": "capability_local_data_storage_a8c07941.function.create_mood_entry",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ]
          },
          {
            "screen_id": "capability_local_data_storage_a8c07941.screen.history",
            "action_id": "capability_local_data_storage_a8c07941.screen-action.load_mood_entries",
            "function_id": "capability_local_data_storage_a8c07941.function.list_mood_entries",
            "table_ids": [
              "capability_local_data_storage_a8c07941.table.mood_entries"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_responsive_single_column_layout_cff0cabc",
      "verification": {
        "valid": true,
        "feature_id": "capability_responsive_single_column_layout_cff0cabc",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_all_interactive_elements_mood_buttons__8a721f94",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_single_column_layout_cff0cabc.screen.check_in",
              "capability_responsive_single_column_layout_cff0cabc.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_text_is_readable_without_zooming_on_sc_2b52d95b",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_single_column_layout_cff0cabc.screen.check_in",
              "capability_responsive_single_column_layout_cff0cabc.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_interface_uses_a_single_column_lay_591091e4",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_single_column_layout_cff0cabc.screen.check_in",
              "capability_responsive_single_column_layout_cff0cabc.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_layout_is_tested_and_functional_on_a9c35cdc",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_single_column_layout_cff0cabc.screen.check_in",
              "capability_responsive_single_column_layout_cff0cabc.screen.history"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_no_sign_up_required_1ded275f",
      "verification": {
        "valid": true,
        "feature_id": "capability_no_sign_up_required_1ded275f",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_no_email_password_or_personal_informat_bb91a172",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_no_sign_up_required_1ded275f.screen.landing"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_app_clearly_communicates_that_data_d9c6ca63",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_no_sign_up_required_1ded275f.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_app_is_fully_functional_without_an_3c6c7676",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_no_sign_up_required_1ded275f.screen.landing",
              "capability_no_sign_up_required_1ded275f.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_users_can_save_and_view_entries_on_fir_29875120",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_no_sign_up_required_1ded275f.screen.landing",
              "capability_no_sign_up_required_1ded275f.screen.history"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_direct_to_check_in_screen_aad4329d",
      "verification": {
        "valid": true,
        "feature_id": "capability_direct_to_check_in_screen_aad4329d",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_link_or_button_to_view_history_is_vi_2f271d5a",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_direct_to_check_in_screen_aad4329d.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_launching_the_app_shows_the_check_in_s_2e4cc2b4",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_direct_to_check_in_screen_aad4329d.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_no_splash_screen_login_or_onboarding_b_eefdf586",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_direct_to_check_in_screen_aad4329d.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_check_in_screen_displays_today_s_d_1d07e467",
            "table_ids": [],
            "function_ids": [
              "capability_direct_to_check_in_screen_aad4329d.function.get_today_date"
            ],
            "screen_ids": [
              "capability_direct_to_check_in_screen_aad4329d.screen.check_in"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_direct_to_check_in_screen_aad4329d.screen.check_in",
            "action_id": "capability_direct_to_check_in_screen_aad4329d.screen-action.load_today_date",
            "function_id": "capability_direct_to_check_in_screen_aad4329d.function.get_today_date",
            "table_ids": []
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_save_mood_entry_d1f7c695",
      "verification": {
        "valid": true,
        "feature_id": "capability_save_mood_entry_d1f7c695",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_clearly_labeled_save_button_is_visib_aab80554",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_mood_entry_d1f7c695.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_clicking_save_writes_the_current_date__a98beeef",
            "table_ids": [
              "capability_save_mood_entry_d1f7c695.table.mood_entries"
            ],
            "function_ids": [
              "capability_save_mood_entry_d1f7c695.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_save_mood_entry_d1f7c695.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_save_is_only_enabled_after_a_mood_has__59675987",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_mood_entry_d1f7c695.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_save_action_completes_in_under_1_s_6d3495e2",
            "table_ids": [
              "capability_save_mood_entry_d1f7c695.table.mood_entries"
            ],
            "function_ids": [
              "capability_save_mood_entry_d1f7c695.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_save_mood_entry_d1f7c695.screen.check_in"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_save_mood_entry_d1f7c695.screen.check_in",
            "action_id": "capability_save_mood_entry_d1f7c695.screen-action.save_mood_entry",
            "function_id": "capability_save_mood_entry_d1f7c695.function.create_mood_entry",
            "table_ids": [
              "capability_save_mood_entry_d1f7c695.table.mood_entries"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_optional_mood_note_f6774e1f",
      "verification": {
        "valid": true,
        "feature_id": "capability_optional_mood_note_f6774e1f",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_text_input_field_is_visible_on_the_c_15a0d0b3",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ],
            "function_ids": [
              "capability_optional_mood_note_f6774e1f.function.get_mood_entries"
            ],
            "screen_ids": [
              "capability_optional_mood_note_f6774e1f.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_leaving_the_field_empty_is_allowed_and_9c78e7f1",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ],
            "function_ids": [
              "capability_optional_mood_note_f6774e1f.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_optional_mood_note_f6774e1f.screen.check_in",
              "capability_optional_mood_note_f6774e1f.screen.history"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_field_accepts_up_to_200_characters_c3c6bdec",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ],
            "function_ids": [
              "capability_optional_mood_note_f6774e1f.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_optional_mood_note_f6774e1f.screen.check_in"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_field_is_clearly_marked_as_optiona_f8ffac48",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ],
            "function_ids": [
              "capability_optional_mood_note_f6774e1f.function.get_mood_entries"
            ],
            "screen_ids": [
              "capability_optional_mood_note_f6774e1f.screen.check_in"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_optional_mood_note_f6774e1f.screen.check_in",
            "action_id": "capability_optional_mood_note_f6774e1f.screen-action.save_mood_entry",
            "function_id": "capability_optional_mood_note_f6774e1f.function.create_mood_entry",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ]
          },
          {
            "screen_id": "capability_optional_mood_note_f6774e1f.screen.history",
            "action_id": "capability_optional_mood_note_f6774e1f.screen-action.load_mood_entries",
            "function_id": "capability_optional_mood_note_f6774e1f.function.get_mood_entries",
            "table_ids": [
              "capability_optional_mood_note_f6774e1f.table.mood_entry"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_five_mood_options_selection_fb56ebd0",
      "verification": {
        "valid": true,
        "feature_id": "capability_five_mood_options_selection_fb56ebd0",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_clicking_a_mood_option_visually_highli_f4fb9f5c",
            "table_ids": [
              "capability_five_mood_options_selection_fb56ebd0.table.mood_entries"
            ],
            "function_ids": [
              "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection"
            ]
          },
          {
            "criterion_id": "criterion_done_when_five_distinct_mood_options_are_display_82c9e96d",
            "table_ids": [
              "capability_five_mood_options_selection_fb56ebd0.table.mood_entries"
            ],
            "function_ids": [
              "capability_five_mood_options_selection_fb56ebd0.function.get_mood_options"
            ],
            "screen_ids": [
              "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection"
            ]
          },
          {
            "criterion_id": "criterion_done_when_only_one_mood_can_be_selected_at_a_tim_c9827793",
            "table_ids": [
              "capability_five_mood_options_selection_fb56ebd0.table.mood_entries"
            ],
            "function_ids": [
              "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry"
            ],
            "screen_ids": [
              "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_selected_mood_is_clearly_indicated_e262353a",
            "table_ids": [
              "capability_five_mood_options_selection_fb56ebd0.table.mood_entries"
            ],
            "function_ids": [
              "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry",
              "capability_five_mood_options_selection_fb56ebd0.function.get_latest_mood_entry"
            ],
            "screen_ids": [
              "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection",
            "action_id": "capability_five_mood_options_selection_fb56ebd0.screen-action.load_mood_options",
            "function_id": "capability_five_mood_options_selection_fb56ebd0.function.get_mood_options",
            "table_ids": []
          },
          {
            "screen_id": "capability_five_mood_options_selection_fb56ebd0.screen.mood_selection",
            "action_id": "capability_five_mood_options_selection_fb56ebd0.screen-action.save_selected_mood",
            "function_id": "capability_five_mood_options_selection_fb56ebd0.function.create_mood_entry",
            "table_ids": [
              "capability_five_mood_options_selection_fb56ebd0.table.mood_entries"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_chronological_history_view_14184bae",
      "verification": {
        "valid": true,
        "feature_id": "capability_chronological_history_view_14184bae",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_history_screen_displays_all_saved_mo_723a0a86",
            "table_ids": [
              "capability_chronological_history_view_14184bae.table.mood_entries"
            ],
            "function_ids": [
              "capability_chronological_history_view_14184bae.function.get_mood_history"
            ],
            "screen_ids": [
              "capability_chronological_history_view_14184bae.screen.history_view"
            ]
          },
          {
            "criterion_id": "criterion_done_when_each_entry_card_shows_the_date_mood_ic_addedf87",
            "table_ids": [
              "capability_chronological_history_view_14184bae.table.mood_entries"
            ],
            "function_ids": [
              "capability_chronological_history_view_14184bae.function.get_mood_history"
            ],
            "screen_ids": [
              "capability_chronological_history_view_14184bae.screen.history_view"
            ]
          },
          {
            "criterion_id": "criterion_done_when_entries_are_shown_in_reverse_chronolog_6fd39cda",
            "table_ids": [
              "capability_chronological_history_view_14184bae.table.mood_entries"
            ],
            "function_ids": [
              "capability_chronological_history_view_14184bae.function.get_mood_history"
            ],
            "screen_ids": [
              "capability_chronological_history_view_14184bae.screen.history_view"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_history_view_is_accessible_from_th_d9b4ab62",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_chronological_history_view_14184bae.screen.history_view"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_chronological_history_view_14184bae.screen.history_view",
            "action_id": "capability_chronological_history_view_14184bae.screen-action.load_history",
            "function_id": "capability_chronological_history_view_14184bae.function.get_mood_history",
            "table_ids": [
              "capability_chronological_history_view_14184bae.table.mood_entries"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_save_confirmation_message_41f550eb",
      "verification": {
        "valid": true,
        "feature_id": "capability_save_confirmation_message_41f550eb",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_confirmation_message_appears_immedia_e4046f0b",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_confirmation_message_41f550eb.screen.check_in_with_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_check_in_form_resets_or_clears_aft_451d71df",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_confirmation_message_41f550eb.screen.check_in_with_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_message_clearly_indicates_the_entr_9811dbac",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_confirmation_message_41f550eb.screen.check_in_with_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_message_is_visible_for_2_3_seconds_e524f11c",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_confirmation_message_41f550eb.screen.check_in_with_confirmation"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    }
  ]
}
```

## Historical validation attempts
```json
{
  "records": [
    {
      "feature_id": "capability_local_data_storage_a8c07941",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:27:31",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_local_data_storage_a8c07941",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "2dca6443099e811dda3d36c9960d35f97e9e31bb59ce1c83785dfd013f39d584",
      "created_at": "2026-09-30 09:28:08",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_local_data_storage_a8c07941",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "39d4bb52cadd687d17273368451731325647113f6897447ad960604a48e6ebf3",
      "created_at": "2026-09-30 09:28:35",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_single_column_layout_cff0cabc",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:29:21",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_single_column_layout_cff0cabc",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "d41e19b748e79d2939505409510663c41c203244d8eb96894c2117a03c2bbf05",
      "created_at": "2026-09-30 09:29:40",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_single_column_layout_cff0cabc",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-09-30 09:30:02",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_no_sign_up_required_1ded275f",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:30:46",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_no_sign_up_required_1ded275f",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "6e1e354c8b061e5dd3dfbeac797b5e438a3402c60759de6ea1ec389dc0dba222",
      "created_at": "2026-09-30 09:31:07",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_no_sign_up_required_1ded275f",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-09-30 09:31:31",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_direct_to_check_in_screen_aad4329d",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:32:16",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_direct_to_check_in_screen_aad4329d",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "1a787d5693f84acde67337ab5f1ac174cc69b86b1dc02ade5b9bf6912d05ab71",
      "created_at": "2026-09-30 09:32:34",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_direct_to_check_in_screen_aad4329d",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "4778ac308485c05c3f755bad62c5606054919769b2fcc09cc432a93fb87af223",
      "created_at": "2026-09-30 09:32:53",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_mood_entry_d1f7c695",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:33:15",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_mood_entry_d1f7c695",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "e84cddd614880a7b76f2d9af6133ccdee42be96de83b09d64ebec2a3d51cfdbd",
      "created_at": "2026-09-30 09:33:37",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_mood_entry_d1f7c695",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "ef1aedbed4513335a482945c951d319f0130baff4dba6f35d0e8c2716175036e",
      "created_at": "2026-09-30 09:33:56",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_optional_mood_note_f6774e1f",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:34:18",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_optional_mood_note_f6774e1f",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "1a21ea815b3f96a8fea6823c90c1b8ad73baf38b12dc2fe714e7c0dad134881e",
      "created_at": "2026-09-30 09:34:42",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_optional_mood_note_f6774e1f",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "96ef33a04fe0148f3a29c5fb20a53c596adc55e803ce3368ee7b4a51bf286633",
      "created_at": "2026-09-30 09:35:21",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_five_mood_options_selection_fb56ebd0",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:35:51",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_five_mood_options_selection_fb56ebd0",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "8c7df741b1b8e4e80d0c40110cc1627109fdb25986c6a30ce90b806750f1e6d8",
      "created_at": "2026-09-30 09:36:21",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_five_mood_options_selection_fb56ebd0",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "ea5a057631c68a4a707a0e73e2061c2026c92c27c9a3a58fde0ca26e914d1b1d",
      "created_at": "2026-09-30 09:36:40",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_chronological_history_view_14184bae",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:37:06",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_chronological_history_view_14184bae",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "e948623d4cde069aad4088d261ae061c88456ca9c079eb2b412c049845c740af",
      "created_at": "2026-09-30 09:37:26",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_chronological_history_view_14184bae",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "a3823c563b02f16538f2c1a142c3024a36f60d7ff3f88534ccf40f1540cee036",
      "created_at": "2026-09-30 09:37:45",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_confirmation_message_41f550eb",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-09-30 09:38:01",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_confirmation_message_41f550eb",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "9cf2d322fb1d484c79f91f17e540dc280429b0e34b69a4e92b72c1564ecc6441",
      "created_at": "2026-09-30 09:38:13",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_confirmation_message_41f550eb",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-09-30 09:38:39",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    }
  ]
}
```

Use feature IDs and the recorded validation details to compare tables, functions and screens. A rejected candidate is not the finalized blueprint. Missing historical details cannot be recovered.
