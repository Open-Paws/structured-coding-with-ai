---
paths:
  - "**/*.html"
  - "**/robots.txt"
  - "**/sitemap.xml"
  - "**/llms.txt"
  - "**/head/**"
  - "**/seo/**"
  - "**/meta/**"
  - "**/schema/**"
  - "**/structured-data/**"
  - "**/layout.*"
  - "**/Layout.*"
  - "**/BaseHead.*"
  - "**/Head.*"
---
# GEO + SEO Rules for Animal Advocacy Websites

Websites built for animal advocacy serve two discovery channels: traditional search engines and AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot). Approximately 60% of searches now end without a click — AI systems are the fastest-growing discovery channel and have distinct citation requirements. Follow these rules when building or modifying any public-facing advocacy website.

## HTML Structure

Every page needs exactly one `<h1>` tag. Use a logical heading hierarchy (`h1 > h2 > h3`), never skipping levels. Phrase `<h2>` headings as questions when the section answers something — question-based headings produce 7× more AI citations for smaller sites. The first paragraph after any heading must directly answer that question in 40-60 words. AI systems pull from the first 30% of content 44% of the time — lead with the answer.

Keep paragraphs to 2-4 sentences (40-60 words). Structure content as self-contained 120-180 word modules — this modular pattern generates 70% more ChatGPT citations than unstructured prose.

Use semantic HTML correctly: `<article>`, `<section>`, `<nav>`, `<aside>`, `<header>`, `<footer>`, `<main>`. Add `lang` attribute to `<html>`. Every `<img>` must have a descriptive `alt` attribute. Every `<a>` must have meaningful anchor text — never "click here".

Use `<table>` for comparison data (32.5% of AI-cited content contains tables). Use `<ol>` and `<ul>` for lists (78% of AI answers include list formats). Use `<blockquote cite="...">` for expert quotations (28-40% AI visibility boost). Use `<time datetime="YYYY-MM-DD">` for dates. Use `<dfn>` for term definitions. Use `<abbr title="full term">` on first use. Add `id` attributes to all `<h2>` and `<h3>` elements.

## Do Not

- Do NOT hide content behind JavaScript-only rendering — AI crawlers often cannot execute JS. All critical content must be in the initial HTML response (SSR or pre-rendered).
- Do NOT use `display:none` or `visibility:hidden` on content to be indexed.
- Do NOT rely on infinite scroll — use paginated `<a>` links.
- Do NOT use iframes for primary content.
- Do NOT keyword-stuff — stuffing decreases AI visibility by 10%.

## Structured Data (JSON-LD)

Implement JSON-LD schema in the `<head>` of every page. Sites with structured data achieve 41% AI citation rates vs 15% without. Only 12.4% of websites implement it — this is the single highest-leverage GEO action.

### Organization + WebSite schema (every page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yoursite.com/#organization",
      "name": "Organization Name",
      "url": "https://yoursite.com",
      "logo": { "@type": "ImageObject", "url": "https://yoursite.com/logo.png" },
      "sameAs": [
        "https://www.linkedin.com/company/your-org",
        "https://twitter.com/your-org",
        "https://github.com/your-org"
      ],
      "description": "One-sentence description"
    },
    {
      "@type": "WebSite",
      "@id": "https://yoursite.com/#website",
      "url": "https://yoursite.com",
      "name": "Site Name",
      "publisher": { "@id": "https://yoursite.com/#organization" }
    }
  ]
}
</script>
```

### Article schema (every content page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Page title",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://yoursite.com/team/author-name",
    "jobTitle": "Their role"
  },
  "publisher": { "@id": "https://yoursite.com/#organization" },
  "datePublished": "2026-01-15T08:00:00Z",
  "dateModified": "2026-03-20T10:30:00Z",
  "image": "https://yoursite.com/images/article-image.jpg",
  "description": "150-160 char meta description"
}
</script>
```

### FAQPage schema (pages with Q&A content)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the question?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Direct, complete answer in 40-80 words."
      }
    }
  ]
}
</script>
```

Also implement when applicable: **HowTo**, **BreadcrumbList**, **SoftwareApplication**, **Event**, **Dataset**, **Person**.

Schema rules: always use JSON-LD (not Microdata). Use `@id` references to connect entities across pages. Keep `dateModified` accurate. Validate at schema.org/validator.

## Meta Tags

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Primary Keyword — Brand Name</title><!-- 50-60 chars, keywords first -->
  <meta name="description" content="150-160 chars. Direct answer + one statistic.">
  <link rel="canonical" href="https://yoursite.com/this-page">
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Description">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://yoursite.com/this-page">
  <meta property="og:image" content="https://yoursite.com/images/og-image.jpg">
  <meta property="og:site_name" content="Site Name">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Page Title">
  <meta name="twitter:description" content="Description">
  <meta name="twitter:image" content="https://yoursite.com/images/twitter-image.jpg">
  <meta property="article:published_time" content="2026-01-15T08:00:00Z">
  <meta property="article:modified_time" content="2026-03-20T10:30:00Z">
</head>
```

Meta description rules: 150-160 chars, direct factual answer to the primary query, one specific statistic, never duplicated across pages.

## Robots.txt

```
# Standard search engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI search and citation crawlers — allow these for AI visibility
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Amazonbot
Allow: /

# AI training crawlers — block if not consenting to training use
# Remove blocks below if maximum AI visibility is the goal
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

# Block scraper bots
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

Sitemap: https://yoursite.com/sitemap.xml
```

Critical: blocking `Googlebot` blocks both Google Search AND AI Overviews — there is no way to allow one without the other. Review quarterly as new crawlers emerge.

## XML Sitemap

Include only canonical, indexable URLs. `<lastmod>` must reflect actual content update date — never fake it. Reference in robots.txt. Submit to Google Search Console and Bing Webmaster Tools. Regenerate automatically when content changes. Maximum 50,000 URLs per file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yoursite.com/</loc>
    <lastmod>2026-03-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

## Site Architecture

URL rules: descriptive hyphenated lowercase, under 75 characters, include primary keyword, max 3 levels deep. Implement canonical tags on every page. Use 301 redirects for URL changes.

Internal linking: no important page more than 3 clicks from homepage. Use hub-and-spoke topic cluster model:
- **Pillar page**: 2,000-4,000 words on a broad topic
- **Cluster pages**: 8-15 detailed pages on specific subtopics
- **Bidirectional links**: every cluster page links to pillar, pillar links to every cluster page

This architecture increases AI citation rates from 12% to 41%.

Content freshness: display "Last Updated: [date]" visibly on every page. Keep `dateModified` synchronized. 76% of the most-cited AI content was updated within 30 days.

## Performance

AI crawlers timeout at 1-5 seconds. Targets:
- TTFB < 200ms
- LCP < 2.5s
- CLS < 0.1
- Page weight < 1MB (18% of pages over 1MB are abandoned by AI crawlers)

Require SSR or SSG — AI crawlers often cannot execute JavaScript. Implement gzip or brotli. Use modern image formats (WebP/AVIF) with `<picture>` fallbacks. Enforce HTTPS.

## Content Patterns That Earn AI Citations

### Citable paragraph pattern

```
[Direct statement of fact]. [Specific statistic with attribution].
[Brief elaboration]. [Source: Named Organization, Date]
```

### FAQ block pattern

Every FAQ section uses `<h2>` or `<h3>` with the exact question, a 40-60 word direct answer immediately after, and FAQPage schema wrapping the section.

### Definition block pattern

```html
<section id="what-is-term">
  <h2>What is [Term]?</h2>
  <p><dfn>[Term]</dfn> is [direct 1-sentence definition]. [Elaboration]. [Attribution].</p>
</section>
```

### Author attribution

Every content page needs a visible author name, credentials, link to an author profile page, and Person schema on that profile. Content with proper author metadata gets cited 40% more.

## Key Statistics

| Signal | Impact |
|--------|--------|
| Adding statistics to claims | +41% AI visibility |
| Citing credible sources inline | +30-40% AI visibility |
| Expert quotations | +28-40% AI visibility |
| Keyword stuffing | -10% AI visibility |
| FAQ schema | 41% citation rate vs 15% without |
| Question-based headings | 7× citation impact for smaller sites |
| 120-180 word modular sections | 70% more ChatGPT citations |
| Content over 2,900 words | 59% more likely to be cited |
| Original or proprietary data | 4.31× more citations per URL |
| Author metadata | +40% citations |
| Topic cluster architecture | Citation rate 12% → 41% |
| Fresh content (updated within 30 days) | 76% of most-cited content |
| Structured data (schema) | 73% higher AI selection rate |
