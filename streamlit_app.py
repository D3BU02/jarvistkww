# Import required libraries
import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(layout="wide")
st.title("🦾 J.A.R.V.I.S")

# Create the main tabs
tab1, tab2 = st.tabs(["Calculators", "Scripts"])

with tab1:
    # Create subtabs for Calculators
    calc1, calc2, calc3 = st.tabs(["Increasing Calculator", "Manual Renewal Calculator", "Discount Off Rate Card"])
    
    with calc1:
        st.header("Increasing Calculator")
        
        # Input for Original ACV
        original_acv = st.number_input("Enter Original ACV (Yearly Rate)", value=3036.00, step=0.01)
        custom_percent = st.number_input("Enter Custom Percentage", value=35.0, step=0.1)
        
        # Calculate increases
        increases = {
            "Original ACV": 0,
            "5% increase": 5,
            "10% increase": 10,
            "15% increase": 15,
            "20% increase": 20,
            "30% increase": 30,
            f"Customized {custom_percent}%": custom_percent
        }
        
        # Create DataFrame
        data = []
        for label, percent in increases.items():
            yearly = original_acv * (1 + percent/100)
            monthly = yearly / 12
            data.append({
                "Calculator": label,
                "Yearly Rate": f"${yearly:,.2f}",
                "Monthly Rate": f"${monthly:,.2f}"
            })
            
        df = pd.DataFrame(data)
        st.dataframe(df, hide_index=True)
    
    with calc2:
        st.header("Manual Renewal Calculator")
        
        # Input fields for each service
        col1, col2 = st.columns(2)
        with col1:
            bundle = st.number_input("Bundle", value=0.0, step=0.01)
            the_knot = st.number_input("The Knot", value=0.0, step=0.01)
            wedding_wire = st.number_input("Wedding Wire", value=0.0, step=0.01)
            buzz = st.number_input("Buzz", value=0.0, step=0.01)
        with col2:
            spotlight = st.number_input("Spotlight", value=0.0, step=0.01)
            city_listing = st.number_input("City Listing", value=0.0, step=0.01)
            venue_listing = st.number_input("Venue Listing", value=0.0, step=0.01)
            custom_renewal_percent = st.number_input("Custom Percentage", value=7.5, step=0.1)
        
        # Calculate totals
        services = {
            "Bundle": bundle,
            "The Knot": the_knot,
            "Wedding Wire": wedding_wire,
            "Buzz": buzz,
            "Spotlight": spotlight,
            "City Listing": city_listing,
            "Venue Listing": venue_listing
        }
        
        # Create first table
        data_renewal = []
        total_current = 0
        total_increase = 0
        
        for service, amount in services.items():
            increase = amount * 0.3
            new_price = amount + increase
            total_current += amount
            total_increase += increase
            data_renewal.append({
                "Service": service,
                "Current Price": f"${amount:,.2f}",
                "30% Increase": f"${increase:,.2f}",
                "New Price": f"${new_price:,.2f}"
            })
        
        data_renewal.append({
            "Service": "Total",
            "Current Price": f"${total_current:,.2f}",
            "30% Increase": f"${total_increase:,.2f}",
            "New Price": f"${(total_current + total_increase):,.2f}"
        })
        
        df_renewal = pd.DataFrame(data_renewal)
        st.dataframe(df_renewal, hide_index=True)
        
        # Calculate different percentage increases
        percentages = [20, 15, 10, 5, custom_renewal_percent]
        total_data = {"Percentage": [], "Total": []}
        
        for pct in percentages:
            total_with_increase = total_current * (1 + pct/100)
            total_data["Percentage"].append(f"{pct}%")
            total_data["Total"].append(f"${total_with_increase:,.2f}")
        
        df_totals = pd.DataFrame(total_data)
        st.subheader("Total Including Percent")
        st.dataframe(df_totals, hide_index=True)
    
    with calc3:
        st.header("Discount Off Rate Card")
        
        # Input for rate card and new rate
        rate_card = st.number_input("Enter Rate Card Price", value=4464.00, step=0.01)
        new_rate = st.number_input("Enter New Rate", value=2654.00, step=0.01)
        
        # Calculate discount
        discount = rate_card - new_rate
        percent_off = (discount / rate_card) * 100 if rate_card else 0
        
        # Display results
        st.write(f"### $ Off Rate Card: ${discount:,.2f}")
        st.write(f"### % Off Rate Card: {percent_off:.2f}%")
        
with tab2:
    # Create subtabs for Scripts
    script1, script2, winback = st.tabs(["Script 1", "Script 2", "Winback Script"])
    
    with script1:
        st.text("Placeholder for Script 1.")
    
    with script2:
        st.text("Placeholder for Script 2.")
    
    with winback:
        st.subheader("Winback Script")
        st.markdown("""
        **Introduction & Acknowledgment:**  
        Hi [Vendor’s Name], this is Michael from Wedding Pro. I wanted to reach out to see how things have been going for your business.  
        I noticed you were previously (...) and we’d love the opportunity to work with you again and support your goals as you continue growing.  

        I’d love to understand a bit more about your experience with us in the past and what led you to step away.  
        Maybe what was working well and what challenges you may have faced would be really helpful.  

        *(Actively listen and validate their experience. Acknowledge any challenges and show empathy if they mention issues with lead volume, cost concerns, or visibility needs.)*  

        **Presenting Solutions & Enhancements:**  
        Thank you for sharing that; I appreciate the insight.  
        Since you were last with us, we’ve made a number of enhancements that could be valuable for you.  

        - **Support:** We created a whole new team to ensure we’re available anytime our vendors need us.  
        - **Leads Problem:** I can share tips to increase visibility and quality leads, including storefront improvements like photos, videos, FAQs, and pricing.  
        - **Reviews:** Build recent testimonials for credibility using your personalized review URL.  
        """)
