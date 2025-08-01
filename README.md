<p align="center">
  <h3 align="center">Targeted Marketing Plan</h3>
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=1A80F7&center=true&vCenter=true&random=true&width=435&lines=Customer+Segmentation;Powered+by+IBM+Granite;RFM+Analysis;Targeted+marketing+strategies" alt="Typing SVG" /></a>
</p>

<p align="center">
    <img alt="Python" title="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
</p>

<p align="center">
    <img alt="Pandas" title="Pandas" src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff"/>
    <img alt="IBM Granite" title="IBM Granite" src="https://img.shields.io/badge/IBM%20Granite%20(via%20Replicate)-E42528?logo=replicate&logoColor=fff"/>
</p>

<p align="center">
    <a href="https://www.canva.com/design/DAGu0-h7F6A/0nbjh28uO48WEnmMdiriQw/edit?utm_content=DAGu0-h7F6A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton">
      <img src="https://custom-icon-badges.demolab.com/badge/-Click%20Me%20to%20View%20Presentation%20(Canva)-9147FF?style=for-the-badge&logoColor=white" title="Slides" alt="Slides"/></a>
</p>

---

### 📖 Background
You are helping a retail company that sells a variety of consumer products. The company has collected detailed sales data from its retail stores and now aims to develop a focused marketing plan to boost performance and increase customer engagement. Your client wants the strategies to be highly targeted, ensuring that marketing efforts reach the right customers with the right message. 

### 🎯 Goal
The goal of this project is to develop a data-driven marketing plan based on retail sales data to improve customer targeting, increase sales, and enhance overall marketing effectiveness. By identifying key customer segments and purchasing patterns, the strategy will focus on delivering the right message to the right audience.

---

### 🧠 Method
<img width="3422" height="2062" alt="Sales Funnel Chart Planning Whiteboard in Yellow Black Tactile 3D Style (2)" src="https://github.com/user-attachments/assets/9cf8b017-4775-488a-b801-2bc1dcf39dec" />

### 🔍 Insight
`Customer Segment based on RFM`
| Customer Segment | Description |
|-----------------|-------------|
| Loyal Customers | Repeat buyers making regular purchases |
| Big Spenders | High-value customers with less frequent but expensive purchases (average ~$500), favoring premium electronics |
| New Customers | Entry-level buyers with low basket size (~$47), likely testing the brand with basic clothing items |
| At Risk | Previously engaged customers who now show signs of drop-off, purchasing cheaper items in bulk but with low average value (~$35) |
| Churned | High-value customers who have stopped purchasing altogether, despite past engagement in premium furniture |

`Customer Profiling`
| Customer Segment | Region | Payment Preference | Most Purchased Category | Most Bought Item | Avg Order Date | Avg Quantity | Cost per Item | Avg Sale Price |
|-----------------|--------|-------------------|----------------------|-----------------|---------------|--------------|--------------|---------------|
| Loyal Customers | Southeast | Credit Card | Clothing | Hats | 2023-02-01 | 7 | Varies | 338 |
| Big Spender | Northeast | Credit Card | Electronics | Phones | 2023-05-20 | 4 | 131-161 | 258-785 |
| New Customers | West | EFT | Clothing | Shirts | 2023-09-09 | 2 | 33.5 | 47 |
| At Risk | West | Credit Card | Clothing | Hats | 2023-10-01 | 7 | 4.71-9 | 21-45 |
| Churned | Northeast | Credit Card | Furniture | Bookcases | 2023-01-25 | 2 | 211 | 662 |

`Customer Persona`
| Customer Segment | Persona Type | Key Traits | Average Purchase | Buyer Characteristic |
|-----------------|--------------|------------|------------------|---------------------|
| Loyal Customers | Repeat Buyer | Southeast region, Credit Card payment, Consistent Clothing purchases, Hats are most bought, avg 7 items, moderate spending | $338 | Brand-attached, Quality-focused |
| Big Spender | High-Value Customer | Northeast region, Credit Card payment, Electronics purchases, Phones are most bought, avg 4 items, high spending | $500 | Brand-attached, Quality-focused, Less price-sensitive |
| New Customers | Price-Sensitive Buyer | West region, EFT payment, Clothing purchases, Shirts are most bought, avg 2 items, low spending | $47 | Price-sensitive, Value-focused |
| At Risk | Declining Value Customer | West region, Credit Card payment, Clothing purchases, Hats are most bought, avg 7 items, low spending | $35 | Price-sensitive, Less brand-attached |
| Churned | Lost High-Value Customer | Northeast region, Credit Card payment, Furniture purchases, Bookcases are most bought, avg 2 items, high spending | $662 | Brand-attached, Quality-focused |


### 💡 Recommendation
| Customer Segment | Recommended Marketing Strategies |
|-----------------|----------------------------------|
| Loyal Customers | - Offer exclusive discounts on hats<br>- Loyalty program rewards<br>- New clothing line notifications |
| Big Spender | - Promote new phone releases<br>- Exclusive access to sales<br>- Premium customer service |
| New Customers | - Provide introductory discounts<br>- Bundle deals on shirts<br>- Free shipping offers |
| At Risk | - Implement win-back campaigns with targeted discounts on hats<br>- Free shipping<br>- Promotional bundles |
| Churned | - Offer personalized re-engagement campaigns<br>- High-value discounts on bookcases<br>- Exclusive access to new furniture lines |

---

### 📁 Project Structure & File Descriptions
📂 `customer_persona/`
Contains JSON files that define marketing personas for each customer segment based on behavior and demographic insights.
- `customer_persona.json` – Consolidated file mapping all buyer personas with attributes like persona type, traits, average spending, and buyer characteristics.

📂 `customer_profile/`
Stores detailed JSON profiles for each customer segment, used to inform targeted marketing strategies.
- `at_risk_customer.json` – Profile data for customers who show declining engagement or reduced purchasing behavior.
- `big_spender_customer.json` – Profile for customers with high purchase value and lower price sensitivity.
- `churned_customer.json` – Profile of customers who were previously active but have stopped buying.
- `loyal_customer.json` – Profile for frequent, repeat buyers with consistent purchasing habits.
- `new_customer.json` – Profile of recent customers with initial low-value purchases.
- `summary.json` – Summary of all customer profiles.

📂 `data/`
Raw and processed data used for analysis and customer segmentation.
- `all_order.xlsx` – Combined order data across all regions, containing customer, product, and transaction details.
- `Customer Orders-East.xlsx` – Filtered order data from the East region.
- `Customer Orders-West.xlsx` – Filtered order data from the West region.
- `Order Details.xlsx` – Detailed transaction-level data including item quantity, unit price, etc.
- `Regions.csv` – Mapping of customer name to regions (e.g., Northeast, Southeast, West).

📂 `LLM Cost Breakdown/`
Analyze LLM usage to estimate cost based on input/output token.
- `llm_cost_breakdown.ipynb` - Notebook to calculate and document the cost breakdown for LLM (Large Language Model) usage.

📓 `data_analysis.ipynb`
Jupyter notebook containing RFM anlaysis and determine marketing strategies.

📓 `data_transform.ipynb`
Notebook used for data preprocessing tasks (e.g., combining sheets, formatting columns).

📄 `llm.py`
Python script containing code to call an LLM model (IBM Granite).

📄 `requirements.txt`
Lists all required Python packages and versions needed to run the notebooks and scripts in this project.

---

### IBM Granite Token Cost Breakdown
| Token Type | Count   | Price per 1M Tokens | Cost             |
| ---------- | ------- | ------------------- | ---------------- |
| Input      | 628,047 | \$0.03              | \$0.01884141     |
| Output     | 26,152  | \$0.25              | \$0.00653800     |
| **Total**  | —       | —                   | **\$0.02537941** |

### Calculation Details
- Input token cost = 628047 × 0.00000003 = $0.01884141
- Output token cost = 26152 × 0.00000025 = $0.006538
- Total cost = $0.01884141 + $0.006538 = $0.02537941

**📁 Cost breakdown is available in `LLM Cost Breakdown`**

---

### Disclaimer
- Customer profiling, persona definitions, and marketing strategies in this project were generated using IBM Granite, a large language model (LLM) developed by IBM.
- All insights and segment characterizations are based on AI-driven analysis of the dataset and may not fully represent real-world customer behaviors.
- Please note that the generated data from language models are probabilistic and may vary depending on input context and model limitations.

### Authors
<p>
    <a href="https://www.linkedin.com/in/salomohendriansudjono/">
       <img alt="Salomo Hendrian Sudjono" title="Salomo Hendrian Sudjono" src="https://custom-icon-badges.demolab.com/badge/-Salomo%20Hendrian%20Sudjono-blue?style=for-the-badge&logo=person-fill&logoColor=white"/>
      </a>
</p>



