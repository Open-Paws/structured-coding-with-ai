# GEO + SEO Rules for Animal Advocacy Websites

Websites built for animal advocacy serve two discovery channels: traditional search engines and AI answer systems (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Bing Copilot). Approximately 60% of searches end without a click — AI systems are the fastest-growing discovery channel and have distinct citation requirements. Follow these rules when building or modifying any public-facing advocacy website.

## HTML Structure

Every page needs exactly one `<h1>` tag containing the primary topic. Use a logical heading hierarchy (`h1 > h2 > h3`), never skipping levels. Phrase `<h2>` headings as questions where the section answers something — question-based headings produce 7× more AI citations for smaller sites. The first paragraph after any heading must directly answer that question in 40-60 words. AI systems pull from the first 30% of content 44% of the time — lead with the answer.

Keep paragraphs to 2-4 sentences (40-60 words). Structure content as self-contained 120-180 word modules — this modular pattern generates 70% more ChatGPT citations than unstructured prose.

Use semantic HTML correctly: `<article>`, `<section>`, `<nav>`, `<aside>`, `<header>`, `<footer>`, `<main>`. Add `lang` attribute to `<html>`. Every `<img>` must have a descriptive `alt` attribute. Every `<a>` must have meaningful anchor text — never "click here".

Use `<table>` for comparison data (32.5% of AI-cited content uses tables). Use `<ol>` and `<ul>` for lists (78% of AI answers include list formats). Use `<blockquote cite="...">` for expert quotations (+28-40% AI visibility). Use `<time datetime="YYYY-MM-DD">` for dates. Use `<dfn>` for term definitions; `<abbr title="...">` for acronyms on first use. Add `id` attributes to all `<h2>` and `<h3>` elements.

Flag any content rendered exclusively by JavaScript. AI crawlers often cannot execute JS — all primary content must be in the initial HTML response (SSR or pre-rendered).

Do NOT use `display:none` or `visibility:hidden` on content to be indexed. Do NOT rely on infinite scroll — use paginated `<a>` links. Do NOT use iframes for primary content. Do NOT keyword-stuff — stuffing decreases AI visibility by 10%.

## Structured Data (JSON-LD)

Structured data is the single highest-leverage GEO action: 41% citation rate with schema vs 15% without. Only 12.4% of websites implement it — a major competitive advantage.

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

Also implement when applicable: HowTo, BreadcrumbList, SoftwareApplication, Event, Dataset, Person. Always use JSON-LD format (not Microdata). Use `@id` references to connect entities across pages. Keep `dateModified` accurate. Validate at schema.org/validator.

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

Meta description: 150-160 chars, direct factual answer to primary query, one specific statistic, never duplicated across pages. Title: `Primary Keyword — Brand Name`, 50-60 chars, keywords first, unique per page.

## Robots.txt

Allow AI citation crawlers, optionally block AI training crawlers:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI citation crawlers — allow for AI answer visibility
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
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

Sitemap: https://yoursite.com/sitemap.xml
```

Note: blocking `Googlebot` blocks both Google Search AND Google AI Overviews — there is no way to separate them.

## XML Sitemap

Include only canonical, indexable URLs. `<lastmod>` must reflect actual update dates — never fake it. Reference in robots.txt. Submit to Google Search Console and Bing Webmaster Tools. Regenerate automatically when content changes.

## Site Architecture

Use descriptive hyphenated lowercase URLs under 75 characters. Max 3 levels deep. Canonical tags on every page. 301 redirects for URL changes.

Hub-and-spoke topic cluster model — increases AI citation rate from 12% to 41%:
- Pillar page: 2,000-4,000 words on a broad topic
- Cluster pages: 8-15 detailed pages on specific subtopics
- Bidirectional links: every cluster page links to the pillar; the pillar links to every cluster page

Display "Last Updated: [date]" visibly using `<time datetime="YYYY-MM-DD">`. Synchronize with `dateModified` in schema. 76% of most-cited AI content was updated within 30 days.

## Performance

AI crawlers timeout at 1-5 seconds: TTFB < 200ms, LCP < 2.5s, CLS < 0.1, page weight < 1MB. Require SSR or SSG — AI crawlers often skip JavaScript rendering. Enforce HTTPS.

## Content Patterns That Earn AI Citations

Citable paragraph pattern:
```
[Direct statement of fact]. [Specific statistic with attribution].
[Brief elaboration]. [Source: Named Organization, Date]
```

FAQ block: `<h2>` with exact question, 40-60 word direct answer immediately following, FAQPage schema wrapping.

Definition block:
```html
<section id="what-is-term">
  <h2>What is [Term]?</h2>
  <p><dfn>[Term]</dfn> is [direct 1-sentence definition]. [Elaboration]. [Attribution].</p>
</section>
```

Author attribution on every content page: visible name, credentials, link to profile page with Person schema. Content with proper author metadata gets 40% more AI citations.

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
