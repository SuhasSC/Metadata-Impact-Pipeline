import streamlit as st
import pandas as pd

st.set_page_config(page_title="Metadata Impact Simulator", layout="wide")
st.title("📊 Metadata Impact Analysis Dashboard")
st.markdown("Upload a CSV file containing `query` and `metadata` columns to compute impact scores.")

uploaded_file = st.file_uploader("📁 Upload CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Check for required columns
        if "query" not in df.columns or "metadata" not in df.columns:
            st.error("❌ The uploaded CSV must have 'query' and 'metadata' columns.")
        else:
            def compute_impact(row):
                query_terms = [term.strip().lower() for term in str(row["query"]).split(',')]
                metadata_terms = [term.strip().lower() for term in str(row["metadata"]).split(',')]
                matches = set(query_terms).intersection(set(metadata_terms))
                score = len(matches) / len(query_terms) if query_terms else 0
                return score

            df["Score"] = df.apply(compute_impact, axis=1)

            # Display Score Statistics
            st.subheader("📈 Impact Score Summary")
            st.metric("Average Score", f"{df['Score'].mean():.2f}")
            st.metric("Minimum Score", f"{df['Score'].min():.2f}")
            st.metric("Maximum Score", f"{df['Score'].max():.2f}")

            # Display Visualization
            if not df.empty and "Score" in df.columns:
                st.subheader("📊 Impact Visualization")
                st.bar_chart(df["Score"])
            else:
                st.warning("⚠️ No valid scores found for visualization.")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("⬆️ Please upload a CSV file to begin.")
