# F45 Held-out Benchmark Results

**Version:** 1.0.0  
**Verified head:** `496f06e0e77438dfb100fcae14e070c146c051fb`  
**Gold Standard CI run:** `32544131890`  
**Artifact:** `f45-heldout-results`  
**Artifact digest:** `sha256:abfcc54c7676f074ea5d1148f7f0b20d34fc8c21f5f186206d495b5bdf8860ea`

## Result

- Scenario count: 8
- Passed: 8
- Pass rate: 1.0
- Python 3.10: PASS
- Python 3.11: PASS
- Python 3.12: PASS

## Held-out scenarios

| Scenario | Expected | Result |
|---|---|---|
| healthy_defensive_response | approved_for_authorized_response | PASS |
| missing_evidence | review_required | PASS |
| chain_of_custody_gap | review_required | PASS |
| critical_not_escalated | review_required | PASS |
| unauthorized_environment | review_required | PASS |
| privacy_review_missing | review_required | PASS |
| unresolved_governance | review_required | PASS |
| awaiting_human_approval | awaiting_human_approval | PASS |

These results validate documented deterministic defensive SOC behaviors. They do not authorize offensive activity or imply universal correctness for every incident, environment, organization, legal regime, or response process.
