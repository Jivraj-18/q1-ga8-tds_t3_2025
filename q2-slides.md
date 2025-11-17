---
marp: true
theme: custom-theme
paginate: true
paginate-position: bottom-right
math: katex
title: Product Documentation Presentation
description: Technical documentation created using Marp
---

<!-- _class: lead -->
<!-- _footer: "*Generated with Marp*" -->

# Product Documentation
### Developer-facing product docs & slides

**Author:** Technical Writer  
**Contact:** <22f3002542@ds.study.iitm.ac.in>

---

# Quick Overview

- Version-controlled single-file presentation  
- Exportable to **HTML**, **PDF**, **PPTX**  
- Themeable and maintainable in Git

---

<!-- _backgroundColor: #0f172a -->

![bg size=cover](https://images.unsplash.com/photo-1518770660439-4636190af475)

# Architecture Overview

- Modular components  
- API-first design  
- Cloud-native deployment

---

# Algorithmic Complexity

A common complexity result used in algorithms:

Inline math example: $T(n) = O(n \log n)$

Displayed math example:

$$
T(n) = \sum_{i=1}^{n} O(\log i) = O(n \log n)
$$

---

<!-- _color: #0033cc -->

# Custom Styling Example

<style scoped>
section {
  background: #eef3ff;
  border-left: 12px solid #0033cc;
  padding: 36px;
}
h1 { color: #002366; }
</style>

This slide demonstrates scoped CSS and a color directive.

---

# Code Example

```js
// Example: fetch docs index
export async function fetchDocsIndex() {
  const res = await fetch('/api/docs/index');
  if (!res.ok) throw new Error('Failed to fetch docs');
  return res.json();
}
