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
CUSTOM THEME
-->
<style>
@theme custom-theme {
  background-color: #ffffff;
  font-family: "Inter", sans-serif;
}

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

---

# Product Documentation  
### Powered by **Marp**

**Author:** Technical Writer  
**Email:** <22f3002542@ds.study.iitm.ac.in>

---

# Overview

- Version-controlled Markdown  
- Reusable documentation  
- Exportable to **HTML**, **PDF**, **PPTX**  
- Supports **Themes**, **Math**, **Code**, **Images**

---

<!-- Background image slide -->
![bg opacity=0.25](https://images.unsplash.com/photo-1518770660439-4636190af475)

# Architecture Overview

- Modular components  
- API-first workflow  
- Cloud-native integration  

---

# Algorithmic Complexity

Using KaTeX math:

$$
T(n) = O(n \log n)
$$

Examples:

- Merge Sort  
  $$O(n \log n)$$

- Binary Search  
  $$O(\log n)$$

---

# Custom Styling Example

<style scoped>
section {
  background: #eef3ff;
  border-left: 12px solid #0033cc;
}
</style>

## Styled Slide

- Scoped CSS only affects this slide  
- Great for callouts or warnings  

---

# Code Example

```js
export async function fetchData() {
  try {
    const res = await fetch("/api/v1/data");
    return await res.json();
  } catch (err) {
    console.error("Fetch failed:", err);
  }
}
