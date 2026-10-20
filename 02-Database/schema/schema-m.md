---
tags: [sml, schema, m, generated]
---
# ตารางกลุ่ม `m` (kbyt)

กลับไป [[schema-index]]

## m_allergic

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| ic_group_main | character varying(25) |
| member_id | character varying(25) |
| symptom | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_bodymassindex

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| bmi | smallint |
| bmi_min | smallint |
| bmi_max | smallint |
| bmi_description | character varying(100) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_congenital_disease

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| member_id | character varying(25) |
| disease | character varying(25) |
| symptom | character varying(100) |
| remark | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_consultation

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| member_id | character varying(25) |
| record_date | timestamp without time zone |
| consultation_detail | character varying(255) |
| doctor | character varying(100) |
| usercreator | character varying(100) |
| status | smallint |
| guid_code | character varying(40) |
| min | smallint |
| max | smallint |
| create_date_time_now | timestamp without time zone |

## m_disease

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| symptom | character varying(255) |
| therapy | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_dozen

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| icode | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_druginteraction

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| item_code_1 | character varying(25) |
| item_code_2 | character varying(25) |
| remark | character varying(255) |
| create_date_time_now | timestamp without time zone |

## m_drugsconsultants

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| member_id | character varying(25) |
| date | timestamp without time zone |
| staff_id | character varying(25) |
| branch_code | character varying(25) |
| remark | character varying(255) |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_drugsconsultants_details

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| date | timestamp without time zone |
| ic_code | character varying(25) |
| times | character varying(100) |
| frequency | character varying(100) |
| warning | character varying(100) |
| properties | character varying(100) |
| qty | smallint |
| remark | character varying(255) |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_frequency

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character(1) |
| create_date_time_now | timestamp without time zone |

## m_healty_standard

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| body_weight_min | smallint |
| body_weight_max | smallint |
| bmi_min | smallint |
| bmi_max | smallint |
| cabondioxide_min | smallint |
| cabondioxide_max | smallint |
| oxygen_min | smallint |
| oxygen_max | smallint |
| bloodpressure_min | smallint |
| bloodpressure_max | smallint |
| heart_rate_min | smallint |
| heart_rate_max | smallint |
| blood_sugar_min | smallint |
| blood_sugar_max | smallint |
| hba1c_min | smallint |
| hba1c_max | smallint |
| cholesterol_min | smallint |
| cholesterol_max | smallint |
| triglyceride_min | smallint |
| triglyceride_max | smallint |
| hdl_min | smallint |
| hdl_max | smallint |
| ldl_min | smallint |
| ldl_max | smallint |
| body_fat_min | smallint |
| body_fat_max | smallint |
| total_protein_min | smallint |
| total_protein_max | smallint |
| albumin_min | smallint |
| albumin_max | smallint |
| globurin_min | smallint |
| globurin_max | smallint |
| uric_acid_min | smallint |
| uric_acid_max | smallint |
| bone_mass_min | smallint |
| bone_mass_max | smallint |
| sodium_min | smallint |
| sodium_max | smallint |
| potassium_min | smallint |
| potassium_max | smallint |
| chloride_min | smallint |
| chloride_max | smallint |
| bun_min | smallint |
| bun_max | smallint |
| creatinine_min | smallint |
| creatinine_max | smallint |
| total_bilirubin_min | smallint |
| total_bilirubin_max | smallint |
| direct_bilirubin_min | smallint |
| direct_bilirubin_max | smallint |
| sgot_ast_min | smallint |
| sgot_ast_max | smallint |
| sgpt_alt_min | smallint |
| sgpt_alt_max | smallint |
| alkaline_phosp_min | smallint |
| alkaline_phosp_max | smallint |
| create_date_time_now | timestamp without time zone |

## m_information

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ic_code | character varying(25) |
| mim_group | character varying(25) |
| common_name | character varying(255) |
| properties | character varying(25) |
| dozen | character varying(25) |
| symptom | character varying(100) |
| warning | character varying(25) |
| remark | character varying(255) |
| times | character varying(25) |
| frequency | character varying(25) |
| keep_methods | character varying(25) |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_kkos

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| min_weight | smallint |
| max_weight | smallint |
| age_min | smallint |
| age_max | smallint |
| probability_osteoporosis | smallint |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_mim_group

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_nationality

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_properties

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_times

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| code | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_warning

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| icode | character varying(25) |
| name_1 | character varying(255) |
| name_2 | character varying(255) |
| status | smallint |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |

## m_yourhealthy

แถวโดยประมาณ: 0

| คอลัมน์ | ชนิด |
|---|---|
| ignore_sync | integer |
| is_lock_record | integer |
| roworder | integer |
| ar_code | character varying(25) |
| member_id | character varying(25) |
| measure_date | timestamp without time zone |
| high | smallint |
| weight | smallint |
| pressure | smallint |
| body_fat | smallint |
| ldl | smallint |
| hdl | smallint |
| triglyceride | smallint |
| cholesterol | smallint |
| kkos | smallint |
| blood_oxygen | smallint |
| bmi | smallint |
| blood_sugar | smallint |
| bun | smallint |
| creatinine | smallint |
| remark | character varying(255) |
| guid_code | character varying(40) |
| create_date_time_now | timestamp without time zone |
