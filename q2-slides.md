---
marp: true
theme: custom-theme
paginate: true
paginate-position: bottom-right
math: katex
title: Product Documentation Presentation
description: Technical documentation created using Marp
---

<!--
Custom Theme (Marp CSS)
Place this theme inside the same file using `<!--` fenced comment blocks.
-->
<style>
section {
  font-family: "Inter", sans-serif;
  padding: 40px;
}
h1 {
  color: #0059ff;
}
h2 {
  color: #003399;
}
p {
  font-size: 1.1rem;
}
footer {
  font-size: 0.8rem;
  color: #666;
}

section strong {
  color: #ff6600;
}
</style>

<!-- Custom Theme Registration -->
<style>
@theme custom-theme {
  background-color: #fdfdfd;
  /* Global font */
  font-family: "Inter", sans-serif;

  /* Slide header underline */
  h1 {
    border-bottom: 3px solid #0059ff;
    padding-bottom: 10px;
  }
}
</style>

---

# Product Documentation  
### Powered by **Marp**

**Author:** Technical Writer  
**Email:** <22f3002542@ds.study.iitm.ac.in>

---

# Overview

- Modern documentation workflow  
- Version-controlled Markdown  
- Exportable to **HTML**, **PDF**, **PPTX**  
- Custom theming and formatting  
- Supports **Math**, **Diagrams**, **Code blocks**

---

# Slide with Background Image

<!-- Use ANY image URL or local file -->
![bg opacity=0.2](https://images.unsplash.com/photo-1518770660439-4636190af475)

## Architecture Overview

- Modular components  
- API-first design  
- Cloud-native deployment

---

# Algorithmic Complexity

Using Marp’s `math: katex` support:

$$
T(n) = O(n \log n)
$$

Examples:

- Merge Sort:  
  $$O(n \log n)$$

- Binary Search:  
  $$O(\log n)$$

---

# Custom Styling

This slide uses **inline custom styles**:

<style scoped>
section {
  background: #f0f4ff;
  border-left: 10px solid #0033cc;
}
</style>

### Key Features

- Theme-based consistency  
- Scoped styling  
- Easy updates via version control

---

# Code Example

```js
export function fetchData() {
  return fetch("/api/v1/data")
    .then(res => res.json())
    .catch(err => console.error(err));
}
