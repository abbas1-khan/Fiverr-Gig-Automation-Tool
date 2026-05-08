import streamlit as st

# Page Configuration
st.set_page_config(page_title="Jari Abbas - Fiverr Portfolio", layout="wide")

# Sidebar - Profile Section
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder icon
st.sidebar.title("Developer Profile")
st.sidebar.markdown("### **Jari Abbas**")
st.sidebar.info("Python Programmer & Automation Expert")

st.sidebar.markdown("---")
st.sidebar.title("Gig Navigation")
step = st.sidebar.radio("Go to Step:", ["1. Overview", "2. Pricing", "3. Description", "4. Requirements"])

# Main Header
st.title("🚀 Jari Abbas - Fiverr Gig Builder")
st.write("Manage and copy your professional gig details from here.")
st.divider()

# --- STEP 1: OVERVIEW ---
if step == "1. Overview":
    st.header("Step 1: Gig Overview")
    st.subheader("Gig Title")
    st.code("I will develop custom Python scripts for automation and web scraping", language="text")
    
    st.subheader("Category")
    st.write("Programming & Tech > Software Development")
    
    st.subheader("Search Tags (SEO)")
    tags = ["Python", "Web Scraping", "Automation", "Selenium", "Data Science"]
    st.success(f"Tags: {', '.join(tags)}")

# --- STEP 2: PRICING ---
elif step == "2. Pricing":
    st.header("Step 2: Scope & Pricing")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🟢 Basic")
        st.write("**Name:** Simple Script")
        st.write("**Price:** $10")
        st.write("**Delivery:** 1 Day")
        st.caption("Perfect for small automation tasks or scraping 1 simple site.")

    with col2:
        st.markdown("### 🟡 Standard")
        st.write("**Name:** Advanced Automation")
        st.write("**Price:** $40")
        st.write("**Delivery:** 3 Days")
        st.caption("Multi-page scraping, data cleaning, or complex task logic.")

    with col3:
        st.markdown("### 🔴 Premium")
        st.write("**Name:** Full-scale Project")
        st.write("**Price:** $100")
        st.write("**Delivery:** 5 Days")
        st.caption("Complex bots or Interactive Streamlit Dashboards with full support.")

# --- STEP 3: DESCRIPTION ---
elif step == "3. Description":
    st.header("Step 3: Gig Description")
    description_text = f"""
Hi! I am Jari Abbas, a professional Python Developer. 

I specialize in:
- Web Scraping (Selenium, BeautifulSoup)
- Task Automation & Scheduling
- Interactive Dashboards (Streamlit)
- Data Processing (Pandas, NumPy)

I provide clean, well-documented code and full support for setup.
Please message me before placing an order!
    """
    st.text_area("Copy this for Fiverr:", value=description_text, height=350)

# --- STEP 4: REQUIREMENTS ---
elif step == "4. Requirements":
    st.header("Step 4: Requirements for Client")
    st.info("Ask these questions to the buyer to start work:")
    st.code("""
1. What is the target website URL?
2. What data fields do you need? (e.g., Name, Price, Email)
3. Preferred output format? (CSV, Excel, JSON)
4. Do you need a Dashboard/GUI or just the script?
    """, language="text")

st.divider()
st.caption("Developed by Jari Abbas | Powered by Streamlit")