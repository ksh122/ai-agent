from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


doc = """ 
    Below is a **comprehensive, up-to-date monetization guideline** for **YouTube, Instagram, and Facebook** focused specifically on *video content*, including considerations 
for *AI-generated videos*, *kids content*, *originality requirements*, and *platform-specific eligibility conditions*. This is structured to help you plan content strategies 
that *comply with policies and maximize monetization potential*.

---

# **1. YouTube Video Monetization Guidelines (2025-2026)**

### **1.1. Eligibility Criteria**

To join the **YouTube Partner Program (YPP)** and earn ad revenue:

* **Reach thresholds**:

  * 1,000 subscribers *and* 4,000 valid public watch hours in the last 12 months,
    **or**
  * 10 million valid *Shorts* views in the last 90 days. ([The Economic Times][1])
* Must adhere to the **YPP monetization policies** and **YouTube Community Guidelines**.

### **1.2. AI-Generated Content Rules**

YouTube **does allow AI tools** to be used in creation, *but monetization requires value-added human involvement*. Key points:

* Fully AI-generated videos with *no human contribution* (scripted, narrated, synthesized, templated) are likely to be deemed **inauthentic** and *ineligible for monetization*.
* Content that uses AI for script, visuals, voice, or editing must include **significant human input**, such as:

  * Original narration or commentary,
  * Human-led storytelling or educational insight,
  * Creative editing and transformation. ([Digital Entire][2])
* Mass-produced AI videos with repetitive structure are likely to be demonetized. ([The Economic Times][1])

### **1.3. Disclosure and Transparency**

* YouTube encourages **disclosure** when synthetic media is used (e.g., AI-generated visuals/voices).
* Misleading audiences with deepfakes or manipulated media can violate policies. ([ReelnReel][3])

### **1.4. Content Quality & Community Compliance**

* Monetization also depends on **advertiser-friendly content**.

  * Avoid prohibited topics (violent, harmful, illegal content).
  * Misleading thumbnails/titles and misinformation can block monetization. ([Digital Marketing Web Design][4])

### **1.5. Kids Content Considerations**

* Videos aimed at children should follow **YouTube's “Made for Kids”** standards:

  * No targeted ads on child-directed material under certain regulations unless properly tagged.
  * Some content restrictions apply due to privacy laws (e.g., COPPA in the U.S.).
* YouTube may limit certain monetization formats for young-audience videos depending on classification.

---

# **2. Instagram Video Monetization Guidelines**

Instagram monetization is part of the broader **Meta Content Monetization Policies**.

### **2.1. Eligibility Conditions**

* Must have a **Professional account** (Creator or Business). ([Boss Wallah Media][5])
* Must be at least **18 years old** to use monetization features. ([Mavely][6])
* Must comply with **Instagram's Community Guidelines** and **Partner Monetization Policies**. ([Instagram Help Center][7])

### **2.2. Ways to Monetize Video Content**

**Instagram offers a range of monetization options:**

1. **Reels Ads / Bonus Programs**

   * Instagram previously tested programs paying creators based on performance of Reels; terminology has evolved into content monetization systems based on views/engagement.

2. **Instagram Subscriptions**

   * Creators can charge followers for exclusive posts/Reels and content access. Typical follower requirement is ~10,000+, though features and criteria vary by region. ([Mavely][6])

3. **Live Badges / Gifts**

   * Viewers buy badges or virtual gifts during live videos or Reels Lives.
   * Badges provide direct revenue. Region-dependent. ([Mavely][6])

4. **Affiliate / Brand Collabs**

   * Affiliate link integrations and branded content tools let creators earn commissions or collaboration fees (not always platform-paid). ([Mavely][6])

### **2.3. Content Requirements**

* Content must be original or feature the creator directly (not just AI/stock footage). ([Facebook][9])
* Monetization tools may be restricted for accounts that primarily post kids-focused content depending on policy interpretation. ([Mavely][6])
* Follow Meta's standards around misinformation, hate speech, copyrighted materials.

---

# **3. Facebook Video Monetization Guidelines**

Facebook (part of Meta) monetizes video content via a suite of tools, largely through the **Meta Content Monetization Program**.

### **3.1. Eligibility & Requirements**

To earn from videos on Facebook:

* Must comply with **Partner Monetization Policies** (Meta). ([Facebook][10])
* Must maintain a legitimate Page or Professional content presence.
* Specific features may require:

  * Minimum total views across videos (some guidance suggests ~30,000 one-minute views). ([Facebook Creators][11])
  * Account established for a minimum period (e.g., 30 days). ([Facebook][10])

### **3.2. Monetization Methods**

1. **In-Stream Ads (Ad Breaks)**

   * Ads shown during longer videos (e.g., >3 minutes).
   * Revenue share between creator and Meta. ([Facebook Creators][12])

2. **Reels & Short Videos**

   * Facebook supports overlay or sticker ads on Reels, driving revenue. ([Wikipedia][13])

3. **Bonuses & Performance Programs**

   * Meta has historically offered bonuses tied to view milestones, depending on region and strategic initiatives. ([Facebook Creators][8])

### **3.3. Content Quality Criteria**

* Original, engaging content performs better; repeated or spammy reposts of existing videos may lose monetization privileges. ([The Verge][14])
* AI-generated content must align with **Community Standards** and must include creative human input if claiming monetized distribution.

---

# **4. Formats & Best Practices Across Platforms (AI/Animation & Kids Content)**

### **4.1. AI-Generated Video Content**

All platforms allow AI assistance, *but the key monetization principle is originality with human contribution*:

* **Do not rely solely on automated generation** with minimal editing (e.g., AI voice reading stock images). ([Simplified][15])
* Use AI for supporting elements (graphics, scripting draft, animation), *but add unique human commentary, voiceover, storytelling, or instructional layer*.
* Consider visual indication or text disclosure of AI involvement for transparency.

### **4.2. Content Styles That Monetize Well**

**For Kids Content:**

* Original animated stories or educational shorts with narration.
* Characters/animations developed by you (not just repurposed clips).
* Comply with child safety standards (no harmful visuals, age-appropriate messaging).

**For Geopolitical & Educational Animation:**

* Tutorial or explainer animations breaking down current affairs in an informative way.
* Use AI to generate visuals but provide **expert narration + sourced insights**.
* Clearly cite sources and distinguish opinion vs. fact.

**For All Formats:**

* Aim for *engagement and watch time metrics* (platforms reward longer average watch time).
* Use **high-quality thumbnails and accurate titles** (misleading clickbait can affect monetization).
* Avoid copyrighted music without license.

---

# **5. Summary of Core Requirements by Platform**

| Platform      | Key Monetization Threshold                                            | AI Content Allowed?               | Originality Requirement                 | Kids Content Consideration            |
| ------------- | --------------------------------------------------------------------- | --------------------------------- | --------------------------------------- | ------------------------------------- |
| **YouTube**   | 1k subs + 4k hours *or* 10M Shorts views                              | Yes, but needs human input        | Strong value/unique commentary required | Must comply with kid content policies |
| **Instagram** | Professional account + age 18+ (+ follower thresholds for some tools) | Yes, original or creator-involved | Direct creator involvement preferred    | Tools may vary by content type        |
| **Facebook**  | Watch hour thresholds + Page compliance                               | Yes with creative input           | Avoid reposts without transformation    | Follow safety standards               |

"""


# Splitting the documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
docs = splitter.split_text(doc)
ids=[]

i=0
for doc in docs:
    ids.append(str(i))
    i=i+1

# Creating DB Client
db_client = chromadb.Client()

# Getting DB collection if not created or create a new one
collection = db_client.get_or_create_collection("rag_db")

# Adding docs to generate embedding 
# Using onnx_models\all-MiniLM-L6-v2 model by default
collection.upsert(
    documents=docs,
    ids = ids
)

# Retrieving top-k results from DB
results = collection.query(
    query_texts=["Instagram Video Monetization Guidelines"],
    n_results=3
)

print(results)