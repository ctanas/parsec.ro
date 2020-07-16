+++
title = "Test"
author = ["Claudiu"]
draft = false
+++

```sql
SELECT to_char(launchDate, 'DD.MM HH24:MI') as "Data", lv_type as "Lansator", lv_prePayload as "Satelit", sat_orbitClass as "Țintă", ls_state as "Țara", lv_name as "Centru", lv_launchpad as "Rampă", lv_outcome as "Rez"
  FROM launches
 WHERE EXTRACT(year FROM "launchdate") = 2019
```