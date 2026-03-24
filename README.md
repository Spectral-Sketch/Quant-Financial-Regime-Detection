# Financial Regime-Shift Detection: Memory-Preserving Risk Indicators
**Auteur:** [A. Schrijvers   ]  
**Focus:** Quantitative Risk Management | Model Validation | Time-Series Engineering  
**Expertise:** 35 jaar ervaring in wiskundige en natuurwetenschappelijke modellering

---

## 🚀 Executive Summary
In de huidige financiële markt is de grootste uitdaging voor risicomodellen het behoud van **marktgeheugen** terwijl data stationair wordt gemaakt voor Machine Learning. Dit project demonstreert een end-to-end pipeline die dit probleem oplost middels **Fractional Differentiation (FracDiff)**. 
<img width="468" height="151" alt="Information Retention" src="https://github.com/user-attachments/assets/80711d73-412f-4d91-83a2-639f945887e2" />


Waar standaard 1ste-orde differentiatie ($d=1$) vaak meer dan 80% van het voorspellende signaal vernietigt, behaalt dit model een **Information Retention Score van 93,82%**.

---

## 🛠 De Architectuur (The Quant Pipeline)

Dit project is opgebouwd uit vier modulaire lagen, precies zoals een professionele productieomgeving bij een grootbank:

### 1. Data Ingestion (`01_Data_Ingest`)
*   **Technologie:** Python (yfinance API).
*   **Actie:** Geautomatiseerde extractie van S&P 500 (SPY) marktdata naar een SQLite omgeving.

### 2. Feature Engineering via SQL (`02_SQL_Engineering`)
*   **Focus:** Berekening van de **Early Warning Indicator** (Moving Volatility).
*   **Expertise:** Gebruik van **SQL Window Functions** (`AVG() OVER...`) om complexe statistiek direct in de database-laag te berekenen.

### 3. De 'Quant Brain' (`03_Quant_Brain`)
*   **Methodiek:** Custom Python implementatie van **Fractional Differentiation** ($d=0.35$).
*   **Resultaat:** Een signaal dat stationair is, maar het lange-termijn geheugen van de tijdreeks behoudt voor het detecteren van **Regime Shifts**.

### 4. Business Intelligence Dashboard (`04_Dashboard`)
*   **Output:** Een 'Executive Dashboard' in Power BI met een dynamische **Early Warning Gauge**.
*   **Business Value:** Risicomanagers zien direct wanneer de marktvolatiliteit drempelwaarden overschrijdt.

---

## 📊 Resultaten
*   **Information Retention:** 93,82% (behoud van voorspellende waarde).
*   **Governance:** Volledig transparante en uitlegbare wiskundige onderbouwing (Explainable AI / XAI).

---

## 📂 Hoe dit project te gebruiken?
1. Voer de Python-scripts uit in de volgorde **01 t/m 03**.
2. Bekijk de SQL-view in DBeaver voor de database-transformatie.
3. Open het `.pbix` bestand in Power BI voor de visuele risico-analyse.
