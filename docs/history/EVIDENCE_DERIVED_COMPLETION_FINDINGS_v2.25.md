# APC v2.25 — Evidence-Derived Completion Findings

## Trigger

The newer compiled package was able to guide a weak/local 9B model much farther through implementation than earlier packages. The remaining weak point became the final mile: integration, actual runtime/browser evidence, and honest completion reporting.

## New invariant

```text
THE FINAL REPORT MUST BE DERIVED FROM
CANONICAL CURRENT STATE + ACTUAL CURRENT EVIDENCE,
NOT FROM THE AMOUNT OF CODE PRODUCED.
```

## Required behavior before COMPLETE

1. reread canonical current State;
2. reread Plan admission/completion rules and Acceptance Matrix;
3. enumerate every requested/master outcome and required criterion;
4. bind each criterion to actual evidence on the current revision;
5. execute missing required build/runtime/browser/user-surface evidence;
6. never substitute file/module/function existence for behavior;
7. never promote package/project-gate, M0, foundation or walking-skeleton success into product completion;
8. invalidate stale evidence after relevant changes;
9. reconcile final status/admission/evidence;
10. only then emit the final report/verdict.

## Why this is not more architecture

The project already has architecture, state, admission and evidence authorities. v2.25 adds a strict final reconciliation over those existing owners rather than creating another completion authority.

## New deterministic negative controls

- foundation/project-gate PASS while required product evidence is absent → FAIL;
- expected implementation file exists but required runtime/browser evidence was never exercised → FAIL;
- relevant source changes after final evidence without re-verification → FAIL.

The goal is to make false completion harder for weaker/long-running agents without adding more generic Governance prose.
