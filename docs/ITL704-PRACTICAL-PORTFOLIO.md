# ITL704 Practical Portfolio: Smart IT Helpdesk

Use this guide to turn the helpdesk into a reviewable Recent Open Source
Project (ROSP) submission. It maps the course activities to work that can be
demonstrated in the application and records which evidence the student group
must create during the semester. Replace the example group roles and dates
with the group's actual information. Do not claim an upstream contribution,
review, deployment, or test result until it has happened.

## Project problem and objective

**Problem statement:** IT support requests arrive through disconnected
channels, making ownership, priority, progress, and resolution history hard to
follow. Build and validate an open-source helpdesk that gives employees a
private request history, engineers a resolution workflow, and administrators
a read-only view of service activity.

**Working model:** This Flask application. The permission boundaries are
enforced on server routes: employees create and follow their own requests,
engineers work the queue, and administrators monitor all requests without
changing tickets. Its application monitoring uses Prometheus metrics and a
Grafana dashboard definition.

**Group:** 3–4 students. Record each member's name, roll number, chosen role,
weekly contribution, evidence link, and supervisor feedback in the logbook
below. Rotate roles so each person demonstrates individual understanding.

## 26-hour implementation plan

The syllabus specifies 26 practical hours. This plan divides them into 13
two-hour lab sessions; place the sessions on the institution's actual calendar.
The group should still update its logbook every week, including weeks without
a scheduled lab. Reviews 1–2 are in Semester 1; reviews 3–4 are in Semester 2.

| Session | Hours | Syllabus module | Planned practical work and evidence |
| --- | ---: | --- | --- |
| 1 | 2 | Prerequisite | Confirm OS, Python, DBMS, IP/network basics; write the problem statement and setup record. |
| 2 | 2 | I: Introduction to OSS | Compare free software and open-source software; inspect the repository license and dependency notices. |
| 3 | 2 | I: Introduction to OSS | Explain GPL/copyleft versus permissive licensing; **Review 1:** problem, group, license, and initial scope. |
| 4 | 2 | II: Contribute to OSS | Identify a real issue or improvement, expected users, acceptance criteria, and a focused branch plan. |
| 5 | 2 | II: Contribute to OSS | Implement a small change, document it, and collect genuine local validation evidence. |
| 6 | 2 | III: Operating systems | Run the app on the group's supported OS; document environment differences and setup. **Review 2:** working model and individual contributions. |
| 7 | 2 | III: Operating systems | Reproduce a bug or usability issue, implement a fix, and record before/after evidence. |
| 8 | 2 | IV: Technologies | Inspect the Flask/SQLAlchemy architecture and identify one technology improvement. |
| 9 | 2 | IV: Technologies | Evaluate the category suggestion feature and its measured limitations; document the chosen improvement. |
| 10 | 2 | V: Network management | Run Prometheus against the app and explain request, error, and latency metrics. **Review 3:** technical progress and evidence quality. |
| 11 | 2 | V: Network management | Import the Grafana dashboard, interpret trends, and record monitoring limitations. |
| 12 | 2 | VI: Applications and cloud services | Deploy a review instance, verify health and role boundaries, and record the live URL and deployment date. |
| 13 | 2 | VI: Applications and cloud services | Validate workflows, complete report and demonstration. **Review 4:** final model, report, and individual viva readiness. |
| **Total** | **26** |  |  |

Keep the Gantt/PERT/CPM chart with actual dates, owners, dependencies, and
completion status. If the supervisor changes this plan, record the change and
reason in the next logbook entry.

## Weekly group logbook

Copy one row per working week. The supervisor should review and sign/comment
on the group's actual entries; do not fill supervisor notes on their behalf.

| Week/date | Student and role | Planned task | Work completed | Individual contribution | Evidence (commit, screenshot, test output, URL) | Blockers / next step | Supervisor note / initials |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

Use repository commits or a change log to distinguish each student's work.
For group discussions, identify who proposed, implemented, reviewed, and
validated each decision.

## Review record

Complete at least two reviews in each semester and retain the committee's
actual questions, feedback, marks, and attendance record.

| Review | Semester/date | Demonstrated work | Individual questions and responses | Feedback / action items | Reviewer names / signatures |
| --- | --- | --- | --- | --- | --- |
| 1 |  | Problem statement, group, license, scope |  |  |  |
| 2 |  | Working model, progress, individual work |  |  |  |
| 3 |  | Technical implementation, monitoring, validation |  |  |  |
| 4 |  | Final model, report, demonstration, viva |  |  |  |

## Required assignments

### Assignment 1 — OSS, free software, and license review

1. Explain the difference between free-of-charge software and software
   freedoms/open-source licensing. Cite the sources consulted.
2. Compare the project's MIT license with GPLv3: permissions, source
   disclosure/copy-left obligations, notices, and redistribution implications.
3. Inspect the direct dependencies and the externally loaded Bootstrap CSS/JS
   asset. Record each exact version, license source, and notice requirement.
4. Explain why the project license does not replace dependency licenses.
5. Submit a one-page conclusion and a source list. Do not say the project is
   GPL-licensed; it is MIT-licensed unless the owner changes it.

**Evidence:** completed comparison, captured license/source links, and
individual oral explanation.

### Assignment 2 — Trace an open-source contribution

1. Find a real bug or improvement in this project or an upstream dependency.
   Explain the user need and acceptance criteria.
2. Check existing issues and contribution guidance. If using an upstream
   project, follow that project's actual contribution rules.
3. Propose at least two solutions, choose one, and explain the trade-offs.
4. Create a focused branch, make the change, add/update validation, and record
   the actual command and output.
5. Prepare a pull request description with problem, changes, evidence, and
   limitations. Link a real issue/PR only if one was actually created.
6. Record any review feedback and revisions. A local exercise is valid
   learning evidence, but it must not be described as an upstream contribution
   or merged PR.

**Evidence:** problem statement, alternatives, branch/commit reference,
validation output, review response, and an honest contribution status.

## Validation and demonstration checklist

- Demonstrate employee ticket creation and confirm an employee cannot read
  another employee's ticket.
- Demonstrate engineer assignment, troubleshooting, resolution, and status
  history.
- Demonstrate that an administrator can inspect the full queue and analytics
  while ticket-changing requests are denied.
- Capture `/healthz`, Prometheus metrics, and the Grafana dashboard with the
  monitoring limitations explained.
- Record test commands and real results, screenshots, deployment URL/date,
  known bugs, and a reproducible setup guide.
- Use synthetic demo records only in a demo deployment. Never expose sample
  passwords or real employee ticket data in a public report.

## Final report structure

1. Abstract and problem statement
2. Survey of existing solutions and identified need
3. OSS/GPL/license and contribution analysis
4. Requirements, use cases, and role/permission matrix
5. Alternatives considered and chosen architecture
6. Gantt/PERT/CPM plan and deviations
7. Implementation with screenshots and individual contribution breakdown
8. Test/validation results, monitoring observations, and limitations
9. Deployment/setup guide and user guide
10. Conclusion, future scope, references, and appendices (logbook, reviews,
    assignments, source links)

## Syllabus outcome coverage

| Learning outcome | Practical evidence in this project |
| --- | --- |
| LO1: OSS concepts | Assignment 1, MIT notice, dependency licensing notes, documented tools. |
| LO2: Contribute to OSS | Assignment 2, contribution workflow, focused change and review evidence. |
| LO3: Operating systems | Reproducible setup and tested OS record; deployment runtime notes. |
| LO4: Technologies | Flask, Python, SQLAlchemy, PostgreSQL, scikit-learn; measured feature limits. |
| LO5: Network management | Prometheus/Grafana service metrics, health check, interpretation and limits. |
| LO6: Applications and services | Role-based helpdesk deployed and demonstrated as a working service. |

This mapping describes a plan and repository artifacts. It does not itself
prove the group completed a contribution, review, deployment, or assessment.
