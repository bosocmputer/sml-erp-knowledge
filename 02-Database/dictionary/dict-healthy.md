---
tags: [sml, dictionary, healthy, generated]
module: Healthy
---
# พจนานุกรม: Healthy — สุขภาพ/ร้านยา

กลับไป [[dictionary-index]]

| ตาราง | ความหมาย | คอลัมน์ |
|---|---|---|
| [[#m_allergic]] | ประวัติแพ้ยา / allergic | 10 |
| [[#m_bodymassindex]] | ดัชนีมวลกาย / ดัชนีมวลกาย | 6 |
| [[#m_congenital_disease]] | โรคประจำตัว / congenital disease | 9 |
| [[#m_consultation]] | ประวัติคำปรึกษาสุขภาพ / Consultation_Health | 11 |
| [[#m_disease]] | ชนิดโรค / disease | 7 |
| [[#m_dozen]] | ขนาดและวิธีใช้ยา / Dozen | 5 |
| [[#m_druginteraction]] | Drug Interaction / Drug Interaction | 5 |
| [[#m_drugsconsultants]] | ประวัติการให้คำปรึกษาการใช้ยา / drugs Consultants | 8 |
| [[#m_drugsconsultants_details]] | ประวัติการให้คำปรึกษาการใช้ยา / drugs Consultants | 12 |
| [[#m_frequency]] | ข้อกำหนดเวลาใช้ยา / ข้อกำหนดเวลาใช้ยา | 5 |
| [[#m_healty_standard]] | ค่ามาตรฐานตัววัดสุขสภาพ / Health_Standard | 66 |
| [[#m_information]] | รายละเอียดยาเพิ่มเติม / รายละเอียดยาเพิ่มเติม | 23 |
| [[#m_kkos]] | ความเสี่ยงกระดูกพรุน / KKOS_scoring | 7 |
| [[#m_mim_group]] | รหัสชื่อกลุมตาม MIM / รหัสชื่อกลุมตาม MIM | 5 |
| [[#m_nationality]] | สัญชาติ / NATIONALITY | 5 |
| [[#m_properties]] | รหัสสรรพคุณยา / Properties | 5 |
| [[#m_times]] | ช่วงเวลาการใช้ยา / time_for_used | 5 |
| [[#m_warning]] | รหัสคำเตือนการใช้ยา / Warning | 5 |
| [[#m_yourhealthy]] | ข้อมูลสุขภาพ / ข้อมูลสุขภาพ | 20 |

## m_allergic

**ประวัติแพ้ยา** — allergic · edition: `ประวัติแพ้ยา`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) |  |
| `ic_group_main` | รหัสกลุ่มสินค้าที่แพ้ยา |  | varchar(25) |  |
| `member_id` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `symptom` | อาการพ้ยา |  | varchar(100) | ✓ |
| `remark` | หมายเหตุเพิ่มเติม |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* | Name | char |  |
| `allergic_name` | กลุ่มยาที่แพ้ *(resource only)* | Allergic Name | char |  |
| `allergic_namegroup` | ชื่อกลุ่มยา *(resource only)* |  | char |  |

index: `m_allergic_PK_PRIMARY_arcode`(ar_code,ic_group_main), `PK_m_allergic_arcode`(ar_code), `PK_m_allergic_groupmain`(ic_group_main)

## m_bodymassindex

**ดัชนีมวลกาย** — ดัชนีมวลกาย · edition: `BMI`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `bmi` | ดัชนีมวลกาย | Body Mass Index | smallint |  |
| `bmi_min` | ดัชนีมวลกายต่ำสุด | Min Body Mass Index | smallint | ✓ |
| `bmi_max` | ดัชนีมวลกายสูงสุด | Max Body Mass Index | smallint | ✓ |
| `bmi_description` | คำอธิบาย | meaning | varchar(100) | ✓ |
| `status` | สถานะ | status | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_bodymassindex_PK_PRIMARY`(bmi)

## m_congenital_disease

**โรคประจำตัว** — congenital disease

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) |  |
| `member_id` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `disease` | รหัสโรค |  | varchar(25) |  |
| `symptom` | อาการโรค |  | varchar(100) | ✓ |
| `remark` | หมายเหตุเพิ่มเติม |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* |  | char |  |
| `disease_name` | ชื่อโรค *(resource only)* |  | char |  |

index: `m_congenital_disease_PK_PRIMARY_congenital_disease_arcode`(ar_code,disease), `PK_m_congenital_disease_arcode`(ar_code), `PK_m_congenital_disease_disease`(disease)

## m_consultation

**ประวัติคำปรึกษาสุขภาพ** — Consultation_Health

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสลูกค้า |  | varchar(25) |  |
| `member_id` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `record_date` | วันที่บันทึก |  | datetime |  |
| `consultation_detail` | รายละเอีดยคำปรึกษา |  | varchar(255) | ✓ |
| `doctor` | หมอที่ให้คำปรึกษา |  | varchar(100) | ✓ |
| `usercreator` | ผู้บันทึก |  | varchar(100) | ✓ |
| `status` | สถาะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* | Name | char |  |
| `min` | Min | Min | smallint | ✓ |
| `max` | Max | Max | smallint | ✓ |

index: `m_consultation_PK_PRIMARY`(ic_code,record_date)

## m_disease

**ชนิดโรค** — disease · edition: `ชนิดโรค`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัสโรค |  | varchar(25) |  |
| `name_1` | ชื่อโรค |  | varchar(255) | ✓ |
| `name_2` | ชื่อโรค(อังกฤษ) |  | varchar(255) | ✓ |
| `symptom` | อาการของโรค |  | varchar(255) | ✓ |
| `therapy` | วิธีการรักษาโรค |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_disease_PK_PRIMARY`(code)

## m_dozen

**ขนาดและวิธีใช้ยา** — Dozen · edition: ` `

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `icode` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่ออังกฤษ |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_dozen_PK_PRIMARY`(icode)

## m_druginteraction

**Drug Interaction** — Drug Interaction

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `item_code_1` | รหัสสินค้า 1 |  | varchar(25) |  |
| `item_code_2` | รหัสสินค้า 2 |  | varchar(25) |  |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `item_name` | ชื่อสินค้า *(resource only)* |  | char |  |
| `item_code` | รหัสสินค้า *(resource only)* |  | char |  |

index: `item_code_1_idx`(item_code_1), `item_code_2_idx`(item_code_2), `item_code_idx`(item_code_1,item_code_2)

## m_drugsconsultants

**ประวัติการให้คำปรึกษาการใช้ยา** — drugs Consultants

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) |  |
| `member_id` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `date` | วันที่ให้คำปรึกษา |  | datetime |  |
| `staff_id` | รหัสพนักงานที่ให้คำปรึกษา |  | varchar(25) | ✓ |
| `branch_code` | รหัสสาขา |  | varchar(25) | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* | Name | char |  |

index: `m_drugsconsultants_PK_PRIMARY`(ar_code,date)

## m_drugsconsultants_details

**ประวัติการให้คำปรึกษาการใช้ยา** — drugs Consultants

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) | ✓ |
| `date` | วันที่ให้คำปรึกษา |  | datetime | ✓ |
| `ic_code` | รหัสสินค้า |  | varchar(25) | ✓ |
| `times` | วิธีการใช้ยา |  | varchar(100) | ✓ |
| `frequency` | เวลาการใช้ยา |  | varchar(100) | ✓ |
| `warning` | คำเตือน |  | varchar(100) | ✓ |
| `properties` | สรรพคุณ |  | varchar(100) | ✓ |
| `qty` | จำนวนที่จ่าย |  | smallint | ✓ |
| `remark` | หมายเหตุ |  | varchar(255) | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ic_name` | ชื่อสินค้า *(resource only)* | Item Name | char |  |
| `unit_name` | หน่วยนับ *(resource only)* | Unit Name | char |  |

## m_frequency

**ข้อกำหนดเวลาใช้ยา** — ข้อกำหนดเวลาใช้ยา

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่อ(อังกฤษ) |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | char | ✓ |

index: `m_frequency_PK_PRIMARY`(code)

## m_healty_standard

**ค่ามาตรฐานตัววัดสุขสภาพ** — Health_Standard

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `body_weight_min` | Body Weight Minimum | Body Weight Minimum | smallint | ✓ |
| `body_weight_max` | Body Weight Maximum | Body Weight Maximum | smallint | ✓ |
| `bmi_min` | Body Mass Index(BMI) Minimum | Body Mass Index(BMI) Minimum | smallint | ✓ |
| `bmi_max` | Body Mass Index(BMI) Maximum | Body Mass Index(BMI) Maximum | smallint | ✓ |
| `cabondioxide_min` | Cabondioxide Minnimum | Cabondioxide Minnimum | smallint | ✓ |
| `cabondioxide_max` | Cabondioxide Maximum | Cabondioxide Maximum | smallint | ✓ |
| `oxygen_min` | % Oxygen Minnimum | oxygen Minnimum | smallint | ✓ |
| `oxygen_max` | % Oxygen  Maximum | oxygen  Maximum | smallint | ✓ |
| `bloodpressure_min` | Blood Pressure Minnimum | Blood Pressure Minnimum | smallint | ✓ |
| `bloodpressure_max` | Blood Pressure Maximum | Blood Pressure Maximum | smallint | ✓ |
| `heart_rate_min` | Heart Rate Minnimum | Heart Rate Minnimum | smallint | ✓ |
| `heart_rate_max` | Heart Rate Maximum | Heart Rate Maximum | smallint | ✓ |
| `blood_sugar_min` | Fasting Blood Sugar(FBS) Minimum | Fasting Blood Sugar Minimum | smallint | ✓ |
| `blood_sugar_max` | Fasting Blood Sugar(FBS) Maxinimum | Fasting Blood Sugar Maxinimum | smallint | ✓ |
| `hba1c_min` | %HbA1C Minnimum | %HbA1C Minnimum | smallint | ✓ |
| `hba1c_max` | %HbA1C Maximum | %HbA1C Maximum | smallint | ✓ |
| `cholesterol_min` | Cholesterol Minimum | Cholesterol Minimum | smallint | ✓ |
| `cholesterol_max` | Cholesterol Maxinimum | Cholesterol Maxinimum | smallint | ✓ |
| `triglyceride_min` | Triglyceride Minimum | Triglyceride Minimum | smallint | ✓ |
| `triglyceride_max` | Triglyceride Maxinimum | Triglyceride Maxinimum | smallint | ✓ |
| `hdl_min` | HDL Minimum | HDL Minimum | smallint | ✓ |
| `hdl_max` | HDL Maxinimum | HDL Maxinimum | smallint | ✓ |
| `ldl_min` | LDL Minimum | LDL Minimum | smallint | ✓ |
| `ldl_max` | LDL Maxinimum | LDL Maxinimum | smallint | ✓ |
| `body_fat_min` | %Body Fat Minimum | %Body Fat Minimum | smallint | ✓ |
| `body_fat_max` | %Body Fat Maxinimum | %Body Fat Maxinimum | smallint | ✓ |
| `total_protein_min` | Total Protein Minimum | Total Protein Minimum | smallint | ✓ |
| `total_protein_max` | Total Protein Maxinimum | Total Protein Maxinimum | smallint | ✓ |
| `albumin_min` | Albumin Minimum | Albumin Minimum | smallint | ✓ |
| `albumin_max` | Albumin Maxinimum | Albumin Maxinimum | smallint | ✓ |
| `globurin_min` | Globurin Minimum | Globurin Minimum | smallint | ✓ |
| `globurin_max` | Globurin Maxinimum | Globurin Maxinimum | smallint | ✓ |
| `uric_acid_min` | Uric Acid Minimum | Uric Acid Minimum | smallint | ✓ |
| `uric_acid_max` | Uric Acid Maxinimum | Uric Acid Maxinimum | smallint | ✓ |
| `bone_mass_min` | Bone Mass Minimum | Bone Mass Minimum | smallint | ✓ |
| `bone_mass_max` | Bone Mass Maxinimum | Bone Mass Maxinimum | smallint | ✓ |
| `sodium_min` | Sodium Minimum | Sodium Minimum | smallint | ✓ |
| `sodium_max` | Sodium Maxinimum | Sodium Maxinimum | smallint | ✓ |
| `potassium_min` | Potassium Minimum | Potassium Minimum | smallint | ✓ |
| `potassium_max` | Potassium Maxinimum | Potassium Maxinimum | smallint | ✓ |
| `chloride_min` | Chloride Minimum | Chloride Minimum | smallint | ✓ |
| `chloride_max` | Chloride Maxinimum | Chloride Maxinimum | smallint | ✓ |
| `bun_min` | BUN Minimum | BUN Minimum | smallint | ✓ |
| `bun_max` | BUN Maxinimum | BUN Maxinimum | smallint | ✓ |
| `creatinine_min` | Creatinine Minimum | Creatinine Minimum | smallint | ✓ |
| `creatinine_max` | Creatinine Maxinimum | Creatinine Maxinimum | smallint | ✓ |
| `total_bilirubin_min` | Total Bilirubin Minimum | Total Bilirubin Minimum | smallint | ✓ |
| `total_bilirubin_max` | Total Bilirubin Maxinimum | Total Bilirubin Maxinimum | smallint | ✓ |
| `direct_bilirubin_min` | Direct Bilirubin Minimum | Direct Bilirubin Minimum | smallint | ✓ |
| `direct_bilirubin_max` | Direct Bilirubin Maxinimum | Direct Bilirubin Maxinimum | smallint | ✓ |
| `sgot_ast_min` | SGOT(AST) Minimum | SGOT(AST) Minimum | smallint | ✓ |
| `sgot_ast_max` | SGOT(AST) Maxinimum | SGOT(AST) Maxinimum | smallint | ✓ |
| `sgpt_alt_min` | SGPT(ALT) Minimum | SGPT(ALT) Minimum | smallint | ✓ |
| `sgpt_alt_max` | SGPT(ALT) Maxinimum | SGPT(ALT) Maxinimum | smallint | ✓ |
| `alkaline_phosp_min` | Alkaline Phosp  Minimum | Alkaline Phosp  Minimum | smallint | ✓ |
| `alkaline_phosp_max` | Alkaline Phosp Maxinimum | Alkaline Phosp Maxinimum | smallint | ✓ |
| `tab_informations` | ค่ามาตรฐานตัววัดสุขสภาพ *(resource only)* | Healty Standard | char |  |
| `tab_body_weight` | Body Weigth *(resource only)* | Body Weigth | char |  |
| `tab_blood_pressure` | Blood Pressure *(resource only)* | Blood Pressure | char |  |
| `tab_blood_sugar` | Blood Sugar *(resource only)* | Blood Sugar | char |  |
| `tab_cholesterol` | Cholesterol *(resource only)* | Cholesterol | char |  |
| `tab_protein` | Protein *(resource only)* | Protein | char |  |
| `tab_uric_acid` | Uric Acid *(resource only)* | Uric Acid | char |  |
| `tab_bone_mass` | Bone Mass *(resource only)* | Bone Mass | char |  |
| `tab_renal_function` | Renal Function *(resource only)* | Renal Function | char |  |
| `tab_liver_function` | Liver Function *(resource only)* | Liver Function | char |  |

## m_information

**รายละเอียดยาเพิ่มเติม** — รายละเอียดยาเพิ่มเติม

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ic_code` | รหัสสินค้า |  | varchar(25) |  |
| `mim_group` | กล่มยาตาม MIM |  | varchar(25) | ✓ |
| `common_name` | ชื่อสามัญทางยา | Common name | varchar(255) | ✓ |
| `properties` | รหัสสรรพคุณ |  | varchar(25) | ✓ |
| `dozen` | วิธีใช้/ขนาดยา |  | varchar(25) | ✓ |
| `symptom` | ใช้เมื่อมีอาการ |  | varchar(100) | ✓ |
| `warning` | รหัสคำเตือน |  | varchar(25) | ✓ |
| `remark` | หมายเหตุเพิ่มเติมวิธีใช้ยา |  | varchar(255) | ✓ |
| `times` | รหัสเวลาที่ใช้ |  | varchar(25) | ✓ |
| `1` | 0=ไม่กำหนด(none) *(resource only)* |  | char |  |
| `2` | 1=ก่อนอาหาร(Before Meal) *(resource only)* |  | char |  |
| `3` | 2=พร้อมอาหาร(With Meal) *(resource only)* |  | char |  |
| `4` | 3=พร้อมอาหาร(After Meal) *(resource only)* |  | char |  |
| `frequency` | ช่วงเวลาที่ใช้ |  | varchar(25) | ✓ |
| `5` | 0=เช้า(Breakfast) *(resource only)* |  | char |  |
| `6` | 1=กลางวัน(Lunch) *(resource only)* |  | char |  |
| `7` | 2=เย็น(Dinner) *(resource only)* |  | char |  |
| `8` | 3=ก่อนนอน(Bed Time) *(resource only)* |  | char |  |
| `keep_methods` | วิธีเก็บรักษา |  | varchar(25) | ✓ |
| `9` | 0=อุณภูมิมห้อง(Room Temerature) *(resource only)* |  | char |  |
| `10` | 1=เก็บในตู้เย็น(Refigerator) *(resource only)* |  | char |  |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ic_name` | ชื่อ *(resource only)* | Name | char |  |

index: `m_information_PK_PRIMARY`(ic_code)

## m_kkos

**ความเสี่ยงกระดูกพรุน** — KKOS_scoring · edition: `ความเสี่ยงกระดูกพรุน`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `min_weight` | น้ำหนักตัว KG.ต่ำสุด |  | smallint | ✓ |
| `max_weight` | น้ำหนักตัว KG.สูงสุด |  | smallint | ✓ |
| `age_min` | อายุ  Year ต่ำสุด |  | smallint | ✓ |
| `age_max` | อายุ  Yearสูงสุด |  | smallint | ✓ |
| `probability_osteoporosis` | โอกาสกระดูกพรุน | Probability_osteoporosis | smallint | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

## m_mim_group

**รหัสชื่อกลุมตาม MIM** — รหัสชื่อกลุมตาม MIM

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่อภาษาอังกฤษ |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_mim_group_PK_PRIMARY`(code)

## m_nationality

**สัญชาติ** — NATIONALITY

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส | code | varchar(25) |  |
| `name_1` | ชื่อ(ภาษาไทย) | Name thai | varchar(255) | ✓ |
| `name_2` | ชื่อ(ภาษาอังกฤษ) | name English | varchar(255) | ✓ |
| `status` | สถานะ | status | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_nationality_PK_PRIMARY`(code)

## m_properties

**รหัสสรรพคุณยา** — Properties

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่ออังกฤษ |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_properties_PK_PRIMARY`(code)

## m_times

**ช่วงเวลาการใช้ยา** — time_for_used

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `code` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่อ(อังกฤษ) |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_times_PK_PRIMARY`(code)

## m_warning

**รหัสคำเตือนการใช้ยา** — Warning

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `icode` | รหัส |  | varchar(25) |  |
| `name_1` | ชื่อ |  | varchar(255) | ✓ |
| `name_2` | ชื่ออังกฤษ |  | varchar(255) | ✓ |
| `status` | สถานะ |  | smallint | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |

index: `m_warning_PK_PRIMARY`(icode)

## m_yourhealthy

**ข้อมูลสุขภาพ** — ข้อมูลสุขภาพ · edition: `ข้อมูลสุขภาพ`

| คอลัมน์ | ความหมาย (ไทย) | English | ชนิด | null |
|---|---|---|---|---|
| `ar_code` | รหัสลูกค้า |  | varchar(25) |  |
| `member_id` | รหัสสมาชิก |  | varchar(25) | ✓ |
| `measure_date` | วันที่บันทึก |  | datetime |  |
| `high` | ส่วนสูง  ซม. | เซ็นติเมตร | smallint | ✓ |
| `weight` | น้ำหนัก  กก. | กิโลกรัม | smallint | ✓ |
| `pressure` | ความดัน  มม. ปรอท |  | smallint | ✓ |
| `body_fat` | %ไขมันร่างกาย | เปอร์เซนต์ไขมันร่างกาย | smallint | ✓ |
| `ldl` | Low-density Lipoproteins |  | smallint | ✓ |
| `hdl` | High-density Lipoproteins |  | smallint | ✓ |
| `triglyceride` | Triglyceride | 0-200 mg/dL | smallint | ✓ |
| `cholesterol` | Cholesterol | 120-240 mg/dL | smallint | ✓ |
| `kkos` | %KKOS | % ความเสี่ยงการเกิดกระดูกพรุน | smallint | ✓ |
| `blood_Oxygen` | ออกซิเจนในเลือด |  | smallint | ✓ |
| `bmi` | ดัชนีมวลกาย |  | smallint | ✓ |
| `blood_sugar` | น้ำตาลในเลือด | mg/dL | smallint | ✓ |
| `bun` | Blood Urea Nitrogen | mg/dL | smallint | ✓ |
| `creatinine` | Creatinine | mg/dL | smallint | ✓ |
| `remark` | คำอธิบายเพิ่ม |  | varchar(255) | ✓ |
| `guid_code` | guid_code | Guid Code | varchar(40) | ✓ |
| `ar_name` | ชื่อ *(resource only)* | Name | char |  |

index: `m_yourhealthy_PK_PRIMARY`(ar_code,measure_date)

