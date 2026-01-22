# Models

This project does not train predictive or causal models.

This is an intentional design decision.

---

## Why No Models?

- The datasets do not support valid causal inference across domains
- Global prediction would require assumptions the data cannot justify
- Modeling on structurally misaligned data would produce misleading results

---

## Purpose of This Directory

This directory exists to:

- make the modeling boundary explicit
- prevent accidental model additions
- document analytical restraint

Future extensions (if assumptions are made explicit) would live here.

---

> Choosing not to model is a form of analytical discipline.
