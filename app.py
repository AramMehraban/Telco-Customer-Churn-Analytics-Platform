from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# 1. APPLICATION CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Customer Churn Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent
FEATURES_FILE = ROOT / "data" / "processed" / "customer_churn_features.csv"
CLEAN_FILE = ROOT / "data" / "processed" / "customer_churn_clean.csv"

BG = "#080610"
PANEL = "#151020"
BORDER = "#AA0BAF"
DARK_PURPLE = "#9B70FF"
LILAC = "#B69EF1"
LIGHT_LILAC = "#E6D9FF"
WHITE = "#FFFFFF"
MUTED = "#C4B5D8"
RED = "#FD2634"
GREEN = "#47EC9A"
ORANGE = "#FFB35C"
BLUE = "#87BCF1"

PAGES = [
    "Executive Overview",
    "Customer Segmentation",
    "Churn Analysis",
    "Revenue Impact",
    "Customer Details",
    "Customer Risk & Retention",
    "Recommendations",
]

PAGE_FILTERS = {
    "Executive Overview": [
        "contract", "internetservice", "churn", "risk_category"
    ],
    "Customer Segmentation": [
        "gender", "partner", "dependents", "contract",
        "internetservice", "tenure_group"
    ],
    "Churn Analysis": [
        "contract", "paymentmethod", "internetservice",
        "tenure_group", "gender"
    ],
    "Revenue Impact": [
        "contract", "risk_category", "churn", "internetservice"
    ],
    "Customer Details": [
        "churn", "contract", "paymentmethod",
        "internetservice", "risk_category", "gender"
    ],
    "Customer Risk & Retention": [
        "risk_category", "contract", "tenure_group",
        "internetservice", "churn"
    ],
    "Recommendations": [
        "contract", "tenure_group", "risk_category",
        "paymentmethod", "internetservice"
    ],
}

RISK_ORDER = [
    "Critical Risk", "High Risk", "Medium Risk", "Low Risk"
]

RISK_COLORS = {
    "Critical Risk": "#BD3447",
    "High Risk": "#FB8C00",
    "Medium Risk": "#FBC02D",
    "Low Risk": "#43A047",
}

STATUS_COLORS = {
    "yes": RED,
    "no": GREEN,
    "Churned": RED,
    "Retained": GREEN,
}


# ============================================================
# 2. DARK THEME
# ============================================================
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {BG};
        color: {WHITE};
    }}

    [data-testid="stHeader"] {{
        background: rgba(5, 5, 9, 0.96);
    }}

    [data-testid="stSidebar"] {{
        background: #0B0B12;
        border-right: 1px solid {BORDER};
    }}

    [data-testid="stSidebar"] * {{
        color: {WHITE};
    }}

    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
        color: {LILAC};
        font-weight: 650;
    }}

    h1, h2, h3, h4 {{
        color: {WHITE} !important;
        letter-spacing: -0.3px;
    }}

    p, label, li {{
        color: #E5DDF3;
    }}

    .hero-title {{
        color: {LIGHT_LILAC};
        font-size: 2.15rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.25rem;
    }}

    .hero-subtitle {{
        color: {MUTED};
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }}

    .section-heading {{
        color: {LIGHT_LILAC};
        font-size: 1.12rem;
        font-weight: 750;
        margin-top: 0.65rem;
        margin-bottom: 0.7rem;
    }}

    .kpi-card {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-top: 3px solid {DARK_PURPLE};
        border-radius: 11px;
        padding: 15px 16px 14px 16px;
        min-height: 112px;
        margin-bottom: 8px;
    }}

    .kpi-label {{
        color: {LILAC};
        font-size: 0.84rem;
        font-weight: 850;
        line-height: 1.35;
        text-transform: uppercase;
        letter-spacing: 0.65px;
        margin-bottom: 12px;
        text-shadow: 0 0 8px rgba(216, 200, 255, 0.12);
    }}

    .kpi-value {{
        color: {LIGHT_LILAC};
        font-size: 1.8rem;
        font-weight: 850;
        line-height: 1.15;
        overflow-wrap: anywhere;
    }}

    .kpi-note {{
        color: {MUTED};
        font-size: 0.76rem;
        margin-top: 8px;
        line-height: 1.35;
    }}

    .insight-card {{
        background: #100D19;
        border: 1px solid {BORDER};
        border-left: 3px solid {DARK_PURPLE};
        border-radius: 9px;
        padding: 13px 15px;
        margin: 7px 0 12px 0;
    }}

    .insight-label {{
        color: {LILAC};
        font-size: 0.77rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.45px;
        margin-bottom: 5px;
    }}

    .insight-text {{
        color: #F0E9FF;
        font-size: 0.91rem;
        line-height: 1.55;
    }}

    .filter-chip {{
        display: inline-block;
        color: {LIGHT_LILAC};
        background: #211532;
        border: 1px solid #513477;
        border-radius: 15px;
        padding: 4px 9px;
        margin: 3px 4px 3px 0;
        font-size: 0.76rem;
    }}

    .info-panel {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 14px 15px;
        margin: 10px 0;
    }}

    .small-muted {{
        color: {MUTED};
        font-size: 0.79rem;
        line-height: 1.5;
    }}

    div[data-testid="stMetric"] {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 12px;
    }}

    div[data-testid="stMetricLabel"] {{
        color: {LILAC};
    }}

    div[data-testid="stMetricValue"] {{
        color: {LIGHT_LILAC};
    }}

    div[data-testid="stExpander"] {{
        border: 1px solid {BORDER};
        border-radius: 8px;
        background: #0D0C14;
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {BORDER};
        border-radius: 8px;
    }}

    .stButton button {{
        border-radius: 8px;
        border: 1px solid #62418D;
        background: #211532;
        color: {LIGHT_LILAC};
        font-weight: 650;
    }}

    .stButton button:hover {{
        border-color: {LIGHT_LILAC};
        color: #FFFFFF;
    }}

    hr {{
        border-color: {BORDER};
    }}

    footer {{
        visibility: hidden;
    }}
    

/* === CHURN INTELLIGENCE: targeted visual refinements === */

/* Lilac sidebar title */
section[data-testid="stSidebar"] h1 {{
    color: #B9A0E8 !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
}}

/* One subtle frame around each chart */
div[data-testid="stPlotlyChart"] {{
    border: 1px solid #D8C9F2 !important;
    border-radius: 12px !important;
    padding: 8px !important;
    box-sizing: border-box !important;
    width: 100% !important;
}}

/* Keep charts within the available width */
div[data-testid="stPlotlyChart"],
div[data-testid="stPlotlyChart"] > div {{
    max-width: 100% !important;
    min-width: 0 !important;
}}

/* Remove bar outlines while preserving the bar fills */
div[data-testid="stPlotlyChart"] .barlayer path {{
    stroke: none !important;
}}
</style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. LOAD AND VALIDATE DATA
# ============================================================
@st.cache_data(show_spinner="Loading customer analytics data...")
def load_data():
    if FEATURES_FILE.exists():
        source = FEATURES_FILE
    elif CLEAN_FILE.exists():
        source = CLEAN_FILE
    else:
        raise FileNotFoundError(
            "Customer data was not found. Expected "
            "data/processed/customer_churn_features.csv "
            "or data/processed/customer_churn_clean.csv."
        )

    data = pd.read_csv(source)
    data.columns = data.columns.str.strip().str.lower()

    required = {
        "customerid", "churn", "contract", "monthlycharges"
    }
    missing = required - set(data.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    data["customerid"] = data["customerid"].astype(str).str.strip()
    data["churn"] = data["churn"].astype(str).str.strip().str.lower()

    for col in [
        "tenure", "monthlycharges", "totalcharges",
        "risk_score", "service_count",
    ]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    if "seniorcitizen" in data.columns:
        data["seniorcitizen"] = data["seniorcitizen"].astype(str)

    if "seniorcitizen_label" not in data.columns and "seniorcitizen" in data.columns:
        data["seniorcitizen_label"] = data["seniorcitizen"].map({
            "0": "Non-Senior",
            "1": "Senior",
            "0.0": "Non-Senior",
            "1.0": "Senior",
        }).fillna(data["seniorcitizen"])

    if "tenure_group" not in data.columns and "tenure" in data.columns:
        data["tenure_group"] = pd.cut(
            data["tenure"],
            bins=[-1, 12, 24, 48, 72],
            labels=[
                "0-12 Months", "13-24 Months",
                "25-48 Months", "49-72 Months",
            ],
        ).astype("string")

    return data, source.name


try:
    df, source_name = load_data()
except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
    st.error(str(exc))
    st.stop()


# ============================================================
# 4. HELPERS
# ============================================================
def money(value):
    return f"${value:,.2f}"


def pct(value):
    return f"{value:.2f}%"


def safe_divide(numerator, denominator):
    return numerator / denominator if denominator else 0.0


def churn_rate(data):
    if data.empty:
        return 0.0
    return safe_divide(
        int(data["churn"].eq("yes").sum()), len(data)
    ) * 100


def group_churn(data, column):
    if column not in data.columns or data.empty:
        return pd.DataFrame()

    result = (
        data.groupby(column, dropna=False)
        .agg(
            Customers=("customerid", "size"),
            Churned=("churn", lambda x: x.eq("yes").sum()),
        )
        .reset_index()
    )
    result["Churn Rate (%)"] = (
        result["Churned"]
        / result["Customers"].replace(0, float("nan"))
        * 100
    ).fillna(0)

    return result


def add_kpi(label, value, note="", value_color="Dark Purpule"):  # +++
    color = value_color or LIGHT_LILAC
    note_html = (
        f'<div class="kpi-note">{note}</div>' if note else ""
    )
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value" style="color:{color}">{value}</div>
            {note_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def kpi_row(items, columns=4):
    cols = st.columns(columns)
    for index, item in enumerate(items):
        with cols[index % columns]:
            add_kpi(*item)


def insight(title, text):
    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-label">{title}</div>
            <div class="insight-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True,
    )


def style_chart(fig, height=350):
    """Apply one consistent style to all dashboard charts."""
    fig.update_layout(
        template="plotly_dark",
        height=height,
        autosize=True,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial, sans-serif",
            color=WHITE,
            size=11,
        ),
        title=dict(
            x=0,
            xanchor="left",
            font=dict(size=16, color="#E6D9FF", family="Arial"),
        ),
        margin=dict(l=20, r=20, t=58, b=35),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#D4D4D8", size=10),
        ),
        colorway=[
            "#A78BFA", "#60A5FA", "#34D399",
            "#FBBF24", "#F87171", "#E879F9",
        ],
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        automargin=True,
        fixedrange=True,
        linecolor=LILAC,
        tickfont=dict(color="#D4D4D8", size=10),
    )

    fig.update_yaxes(
        gridcolor="#30253F",
        zeroline=False,
        automargin=True,
        fixedrange=True,
        tickfont=dict(color="#D4D4D8", size=10),
    )

    return fig


def show_chart(fig, height=350):
    """Display every Plotly chart with consistent dimensions."""
    fig = style_chart(fig, height=height)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "responsive": True,
            "displayModeBar": False,
            "scrollZoom": False,
        },
    )


def chart_divider():
    """Display a subtle divider between dashboard sections."""
    st.markdown(
        """
        <div style="
            width: 100%;
            border-top: 1px solid #B9A0E8;
            margin: 12px 0 20px 0;
            opacity: 0.85;
        "></div>
        """,
        unsafe_allow_html=True,
    )

def chart_empty(message="No data available for this chart."):
    st.info(message)


def best_segment(data, column):
    result = group_churn(data, column)
    if result.empty:
        return None
    result = result[result["Customers"] > 0]
    if result.empty:
        return None
    return result.sort_values(
        ["Churn Rate (%)", "Customers"], ascending=[False, False]
    ).iloc[0]


def select_existing(columns):
    return [col for col in columns if col in df.columns]


def customer_table(data, columns=None, key="customer_table"):
    if columns is None:
        columns = [
            "customerid", "churn", "risk_category", "risk_score",
            "contract", "tenure", "internetservice",
            "paymentmethod", "monthlycharges", "totalcharges",
        ]

    columns = [col for col in columns if col in data.columns]
    if not columns:
        st.info("No supported customer detail columns are available.")
        return

    st.dataframe(
        data[columns],
        use_container_width=True,
        hide_index=True,
        height=360,
        key=key,
    )

    st.download_button(
        "Download table as CSV",
        data=data[columns].to_csv(index=False).encode("utf-8-sig"),
        file_name="customer_churn_analysis.csv",
        mime="text/csv",
        key=f"{key}_download",
    )


# ============================================================
# 5. PAGE NAVIGATION AND PAGE-SPECIFIC FILTERS
# ============================================================
st.sidebar.markdown(
    '<div class="hero-title" style="font-size:1.3rem">CHURN<br>INTELLIGENCE</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("""<div style="color:#D8C8FF;font-size:0.95rem;font-weight:750;line-height:1.5;margin-top:8px;">Customer Analytics &amp; Retention Platform</div>""", unsafe_allow_html=True)
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    PAGES,
    index=0,
    key="page_navigation",
)

page_key = page.replace(" ", "_").replace("&", "and")
page_columns = select_existing(PAGE_FILTERS[page])


def filter_key(column, value):
    return f"filter__{page_key}__{column}__{str(value)}"


def clear_page_filters():
    for column in page_columns:
        for value in df[column].dropna().unique():
            st.session_state[filter_key(column, value)] = False


def reset_page_filters():
    for column in page_columns:
        for value in df[column].dropna().unique():
            st.session_state[filter_key(column, value)] = True


st.sidebar.markdown("### Page Filters")
st.sidebar.caption("Expand a filter and tick the values you want to include.")

for column in page_columns:
    values = sorted(
        df[column].dropna().unique().tolist(),
        key=lambda value: str(value).lower(),
    )

    with st.sidebar.expander(column.replace("_", " ").title(), expanded=False):
        for value in values:
            st.checkbox(
                str(value),
                value=True,
                key=filter_key(column, value),
            )

clear_col, reset_col = st.sidebar.columns(2)

with clear_col:
    st.button(
        "Clear Filters",
        key=f"clear__{page_key}",
        use_container_width=True,
        on_click=clear_page_filters,
    )

with reset_col:
    st.button(
        "Reset Filters",
        key=f"reset__{page_key}",
        use_container_width=True,
        on_click=reset_page_filters,
    )


# Apply the page's selected checkbox values.
filtered = df.copy()
active_filters = []

for column in page_columns:
    values = sorted(
        df[column].dropna().unique().tolist(),
        key=lambda value: str(value).lower(),
    )

    selected = [
        value for value in values
        if st.session_state.get(filter_key(column, value), True)
    ]

    if selected and len(selected) < len(values):
        filtered = filtered[filtered[column].isin(selected)]
        active_filters.append(
            (column.replace("_", " ").title(), selected)
        )
    elif not selected:
        # Clear Filters means show all data without restricting this field.
        pass

st.sidebar.divider()
st.sidebar.markdown("### Active Filters")

if active_filters:
    for label, values in active_filters:
        shown = ", ".join(map(str, values))
        if len(shown) > 85:
            shown = shown[:82] + "..."
        st.sidebar.markdown(
            f'<span class="filter-chip">{label}: {shown}</span>',
            unsafe_allow_html=True,
        )
else:
    st.sidebar.caption("No restrictive filters selected.")

st.sidebar.caption(f"Rows displayed: {len(filtered):,} / {len(df):,}")


# ============================================================
# 6. GLOBAL HEADER
# ============================================================
st.markdown(
    '<div class="hero-title">Customer Churn Analytics Platform</div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="hero-subtitle">{page} · '
    'Business Intelligence, Customer Analytics & Retention</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="small-muted">
        Data source: <b>{source_name}</b> &nbsp; | &nbsp;
        Dataset records: <b>{len(df):,}</b> &nbsp; | &nbsp;
        Filtered records: <b>{len(filtered):,}</b>
    </div>
    """,
    unsafe_allow_html=True,
)
st.divider()


# Common measures calculated on the current page's filtered data.
total = len(filtered)
churned_mask = filtered["churn"].eq("yes")
retained_mask = filtered["churn"].eq("no")
churned_count = int(churned_mask.sum())
retained_count = int(retained_mask.sum())
rate = churn_rate(filtered)
monthly_total = filtered["monthlycharges"].sum()
churned_monthly = filtered.loc[
    churned_mask, "monthlycharges"
].sum()

if "risk_category" in filtered.columns:
    high_mask = filtered["risk_category"].isin(
        ["Critical Risk", "High Risk"]
    )
    critical_mask = filtered["risk_category"].eq("Critical Risk")
else:
    high_mask = pd.Series(False, index=filtered.index)
    critical_mask = pd.Series(False, index=filtered.index)

active_high_mask = retained_mask & high_mask
active_high_count = int(active_high_mask.sum())
active_high_revenue = filtered.loc[
    active_high_mask, "monthlycharges"
].sum()



# ============================================================
# PAGE 1: EXECUTIVE OVERVIEW
# ============================================================
if page == "Executive Overview":
    section("Executive KPI Overview")

    kpi_row([
        ("Total Customers", f"{total:,}", "Customers in current selection"),
        ("Churn Rate", pct(rate), "Share of selected customers", RED),
        ("Churned Customers", f"{churned_count:,}", "Customers marked as churned"),
        ("Monthly Charges", money(monthly_total), "Current monthly charge total"),
    ])

    # --------------------------------------------------------
    # ROW 1: CUSTOMER RETENTION AND CONTRACT CHURN
    # --------------------------------------------------------
    left, right = st.columns(2)

    with left:
        section("Customer Retention Mix")

        if total:
            pie_data = pd.DataFrame({
                "Status": ["Retained", "Churned"],
                "Customers": [retained_count, churned_count],
            })

            fig = px.pie(
                pie_data,
                names="Status",
                values="Customers",
                hole=0.62,
                title="Retained vs Churned Customers",
                color="Status",
                color_discrete_map={
                    "Retained": GREEN,
                    "Churned": RED,
                },
            )

            fig.update_traces(
                textposition="inside",
                textinfo="percent+label",
                marker=dict(line=dict(color=BG, width=2)),
            )

            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Churn Rate by Contract")

        result = group_churn(filtered, "contract")

        if not result.empty:
            fig = px.bar(
                result,
                x="contract",
                y="Churn Rate (%)",
                text=result["Churn Rate (%)"].map(
                    lambda x: f"{x:.1f}%"
                ),
                color="contract",
                title="Contract Type Comparison",
            )

            fig.update_traces(
                textposition="outside",
                cliponaxis=False,
            )

            show_chart(fig)
        else:
            chart_empty()

    # --------------------------------------------------------
    # LILAC DIVIDER BETWEEN CHART ROWS
    # --------------------------------------------------------
    chart_divider()

    # --------------------------------------------------------
    # ROW 2: CUSTOMER RISK AND MONTHLY CHARGES
    # --------------------------------------------------------
    left, right = st.columns(2)

    with left:
        section("Risk Portfolio")

        if "risk_category" in filtered.columns:
            risk_data = (
                filtered["risk_category"]
                .value_counts()
                .reindex(RISK_ORDER, fill_value=0)
                .rename_axis("Risk Category")
                .reset_index(name="Customers")
            )

            fig = px.bar(
                risk_data,
                x="Risk Category",
                y="Customers",
                color="Risk Category",
                title="Customer Count by Risk Level",
                color_discrete_map=RISK_COLORS,
            )

            fig.update_layout(showlegend=False)
            show_chart(fig)
        else:
            chart_empty("Risk categories are not available.")

    with right:
        section("Monthly Charges: Churned vs Retained")

        revenue_data = pd.DataFrame({
            "Status": ["Retained", "Churned"],
            "Monthly Charges": [
                filtered.loc[retained_mask, "monthlycharges"].sum(),
                filtered.loc[churned_mask, "monthlycharges"].sum(),
            ],
        })

        fig = px.bar(
            revenue_data,
            x="Status",
            y="Monthly Charges",
            color="Status",
            title="Monthly Charges by Customer Status",
            color_discrete_map={
                "Retained": GREEN,
                "Churned": RED,
            },
        )

        show_chart(fig)

    # --------------------------------------------------------
    # BUSINESS INSIGHTS
    # --------------------------------------------------------
    contract = best_segment(filtered, "contract")

    if contract is not None:
        insight(
            "KEY BUSINESS INSIGHT",
            f"The highest observed churn rate among contract groups is "
            f"{contract['contract']}: "
            f"{contract['Churn Rate (%)']:.1f}% "
            f"across {int(contract['Customers']):,} customers. "
            "Prioritize contract-specific retention tests rather than "
            "assuming every customer has the same churn risk.",
        )

    insight(
        "BUSINESS ACTION",
        f"Use the current churn rate of {rate:.2f}% as a baseline. "
        "Review month-to-month customers and high-risk active accounts "
        "first, then measure whether retention campaigns reduce churn.",
    )



# ============================================================
# PAGE 2: CUSTOMER SEGMENTATION
# ============================================================
elif page == "Customer Segmentation":
    section("Customer Portfolio & Segment Profile")

    avg_tenure = (
        filtered["tenure"].mean()
        if "tenure" in filtered.columns and total else 0
    )
    partner_share = (
        filtered["partner"].astype(str).str.lower().eq("yes").mean() * 100
        if "partner" in filtered.columns and total else 0
    )
    avg_monthly = (
        filtered["monthlycharges"].mean() if total else 0
    )

    kpi_row([
        ("Customers in Segments", f"{total:,}", "Filtered customer population"),
        ("Average Tenure", f"{avg_tenure:.1f} months", "Customer relationship length"),
        ("Average Monthly Charge", money(avg_monthly), "Average charge per customer"),
        ("Customers with Partner", pct(partner_share), "Share where partner data is available"),
    ])

    left, right = st.columns(2)

    with left:
        section("Contract Segment Mix")
        if "contract" in filtered.columns and total:
            fig = px.pie(
                filtered,
                names="contract",
                title="Customer Share by Contract",
                hole=0.58,
            )
            fig.update_traces(textinfo="percent+label")
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Segment Size by Internet Service")
        if {"contract", "internetservice"}.issubset(filtered.columns):
            tree_data = (
                filtered.groupby(
                    ["contract", "internetservice"], dropna=False
                )
                .size()
                .reset_index(name="Customers")
            )
            fig = px.treemap(
                tree_data,
                path=["contract", "internetservice"],
                values="Customers",
                title="Contract and Internet Service Segments",
                color="Customers",
                color_continuous_scale=["#211532", "#7C3AED", "#C4B5FD"],
            )
            show_chart(fig)
        else:
            chart_empty()

    chart_divider()
    left, right = st.columns(2)

    with left:
        section("Churn Rate by Tenure Group")
        result = group_churn(filtered, "tenure_group")
        if not result.empty:
            order = [
                "0-12 Months", "13-24 Months",
                "25-48 Months", "49-72 Months",
            ]
            result["_order"] = result["tenure_group"].astype(str).map(
                {value: index for index, value in enumerate(order)}
            )
            result = result.sort_values("_order")
            fig = px.bar(
                result,
                x="tenure_group",
                y="Churn Rate (%)",
                title="Tenure and Churn Relationship",
                color="Churn Rate (%)",
                color_continuous_scale=["#6D28D9", "#C4B5FD"],
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Tenure vs Monthly Charges")
        if {"tenure", "monthlycharges"}.issubset(filtered.columns):
            sample = filtered
            if len(sample) > 2500:
                sample = sample.sample(2500, random_state=42)
            fig = px.scatter(
                sample,
                x="tenure",
                y="monthlycharges",
                color="churn",
                hover_data=["contract"],
                title="Customer Tenure and Monthly Charges",
                color_discrete_map=STATUS_COLORS,
                opacity=0.68,
            )
            show_chart(fig)
        else:
            chart_empty()

    segment = best_segment(filtered, "tenure_group")
    if segment is not None:
        insight(
            "SEGMENT INSIGHT",
            f"The tenure group with the highest observed churn rate is "
            f"{segment['tenure_group']} at "
            f"{segment['Churn Rate (%)']:.1f}%. "
            "Compare this group's size and revenue contribution before "
            "allocating retention resources.",
        )

    insight(
        "SEGMENTATION ACTION",
        "Build distinct engagement strategies for new customers, "
        "established customers, and long-tenure customers. "
        "Evaluate churn rate and customer value together; segment size "
        "alone is not a measure of business priority.",
    )


# ============================================================
# PAGE 3: CHURN ANALYSIS
# ============================================================
elif page == "Churn Analysis":
    section("Churn Drivers & Behavioural Patterns")

    month_to_month = (
        filtered["contract"].eq("Month-to-month")
        if "contract" in filtered.columns
        else pd.Series(False, index=filtered.index)
    )
    m2m_rate = churn_rate(filtered[month_to_month])

    churned_avg_charge = (
        filtered.loc[churned_mask, "monthlycharges"].mean()
        if churned_count else 0
    )
    retained_avg_charge = (
        filtered.loc[retained_mask, "monthlycharges"].mean()
        if retained_count else 0
    )

    kpi_row([
        ("Churned Customers", f"{churned_count:,}", "Customers with churn = yes"),
        ("Overall Churn Rate", pct(rate), "Current filtered population", RED),
        ("Month-to-Month Churn Rate", pct(m2m_rate), "Rate within this contract group"),
        ("Avg Charge: Churned", money(churned_avg_charge), "Monthly charges per churned customer"),
    ])

    left, right = st.columns(2)

    with left:
        section("Churn by Contract")
        result = group_churn(filtered, "contract")
        if not result.empty:
            fig = px.bar(
                result,
                x="contract",
                y="Churn Rate (%)",
                color="Churn Rate (%)",
                color_continuous_scale=["#6D28D9", "#F87171"],
                title="Churn Rate Across Contract Types",
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Churn by Payment Method")
        result = group_churn(filtered, "paymentmethod")
        if not result.empty:
            fig = px.bar(
                result.sort_values("Churn Rate (%)", ascending=False),
                x="paymentmethod",
                y="Churn Rate (%)",
                title="Payment Method and Churn",
                color="Churn Rate (%)",
                color_continuous_scale=["#6D28D9", "#F87171"],
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    chart_divider()
    left, right = st.columns(2)

    with left:
        section("Churn by Internet Service")
        result = group_churn(filtered, "internetservice")
        if not result.empty:
            fig = px.bar(
                result,
                x="internetservice",
                y="Churn Rate (%)",
                title="Internet Service and Churn",
                color="internetservice",
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Churn by Tenure")
        if "tenure" in filtered.columns and total:
            tenure_data = (
                filtered.assign(
                    tenure_band=pd.cut(
                        filtered["tenure"],
                        bins=[-1, 6, 12, 24, 36, 48, 60, 72],
                        labels=[
                            "0-6", "7-12", "13-24", "25-36",
                            "37-48", "49-60", "61-72",
                        ],
                    )
                )
                .groupby("tenure_band", observed=False)
                .agg(
                    Customers=("customerid", "size"),
                    Churned=("churn", lambda x: x.eq("yes").sum()),
                )
                .reset_index()
            )
            tenure_data["Churn Rate (%)"] = (
                tenure_data["Churned"]
                / tenure_data["Customers"].replace(0, float("nan"))
                * 100
            ).fillna(0)
            fig = px.line(
                tenure_data,
                x="tenure_band",
                y="Churn Rate (%)",
                markers=True,
                title="Churn Rate Across Tenure Bands",
                hover_data=["Customers", "Churned"],
            )
            fig.update_traces(
                line=dict(color=LILAC, width=2.5),
                marker=dict(size=7, color="#A78BFA"),
            )
            show_chart(fig)
        else:
            chart_empty()

    if churned_count and retained_count:
        gap = churned_avg_charge - retained_avg_charge
        insight(
            "BEHAVIOURAL INSIGHT",
            f"Churned customers have average monthly charges of "
            f"{money(churned_avg_charge)}, compared with "
            f"{money(retained_avg_charge)} for retained customers. "
            f"The observed difference is {money(gap)} per month. "
            "This is an association, not proof that higher charges cause churn.",
        )

    insight(
        "ANALYTICAL ACTION",
        "Investigate the highest-rate contract, payment, and tenure segments. "
        "Validate segment sizes and compare results over time before "
        "treating a small segment's churn rate as a stable pattern.",
    )


# ============================================================
# PAGE 4: REVENUE IMPACT
# ============================================================
elif page == "Revenue Impact":
    section("Revenue Exposure & Customer Economics")

    revenue_at_risk = active_high_revenue
    total_churned_charges = churned_monthly
    average_churned_charge = (
        filtered.loc[churned_mask, "monthlycharges"].mean()
        if churned_count else 0
    )

    kpi_row([
        ("Total Monthly Charges", money(monthly_total), "Selected customer population"),
        ("Charges of Churned Customers", money(total_churned_charges), "Monthly charge total for churned accounts"),
        ("Active High/Critical Risk Charges", money(revenue_at_risk), "Monthly charges of retained high-risk customers"),
        ("Avg Churned Customer Charge", money(average_churned_charge), "Monthly charge per churned customer"),
    ])

    st.caption(
        "These values describe monthly charges, not recognized accounting revenue, "
        "profit, or guaranteed future losses. Risk exposure is a prioritization estimate."
    )

    left, right = st.columns(2)

    with left:
        section("Monthly Charges by Customer Status")
        revenue_data = pd.DataFrame({
            "Status": ["Retained", "Churned"],
            "Monthly Charges": [
                filtered.loc[retained_mask, "monthlycharges"].sum(),
                filtered.loc[churned_mask, "monthlycharges"].sum(),
            ],
        })
        fig = px.bar(
            revenue_data,
            x="Status",
            y="Monthly Charges",
            color="Status",
            title="Monthly Charges by Status",
            color_discrete_map={"Retained": GREEN, "Churned": RED},
            text_auto=".2s",
        )
        show_chart(fig)

    with right:
        section("Revenue Exposure by Risk Level")
        if "risk_category" in filtered.columns:
            risk_revenue = (
                filtered.groupby("risk_category", dropna=False)
                .agg(
                    Customers=("customerid", "size"),
                    Monthly_Charges=("monthlycharges", "sum"),
                )
                .reset_index()
            )
            risk_revenue = risk_revenue.rename(
                columns={
                    "risk_category": "Risk Category",
                    "Monthly_Charges": "Monthly Charges",
                }
            )
            fig = px.treemap(
                risk_revenue,
                path=["Risk Category"],
                values="Monthly Charges",
                color="Risk Category",
                color_discrete_map=RISK_COLORS,
                title="Monthly Charges by Risk Category",
                hover_data=["Customers"],
            )
            show_chart(fig)
        else:
            chart_empty("Risk categories are not available.")

    chart_divider()
    left, right = st.columns(2)

    with left:
        section("Monthly Charges vs Total Charges")
        if "totalcharges" in filtered.columns:
            sample = filtered
            if len(sample) > 2500:
                sample = sample.sample(2500, random_state=42)
            fig = px.scatter(
                sample,
                x="tenure" if "tenure" in sample.columns else "monthlycharges",
                y="totalcharges",
                color="churn",
                size="monthlycharges",
                hover_data=["contract"],
                title="Customer Charge Profile",
                color_discrete_map=STATUS_COLORS,
                opacity=0.65,
            )
            show_chart(fig)
        else:
            chart_empty("Total charges are not available.")

    with right:
        section("Average Monthly Charges by Contract")
        if "contract" in filtered.columns:
            contract_revenue = (
                filtered.groupby("contract", dropna=False)
                .agg(
                    Average_Charge=("monthlycharges", "mean"),
                    Customers=("customerid", "size"),
                )
                .reset_index()
            )
            fig = px.bar(
                contract_revenue,
                x="contract",
                y="Average_Charge",
                title="Average Monthly Charges by Contract",
                hover_data=["Customers"],
                color="Average_Charge",
                color_continuous_scale=["#6D28D9", "#C4B5FD"],
            )
            fig.update_layout(yaxis_title="USD ($)")
            show_chart(fig)
        else:
            chart_empty()

    insight(
        "REVENUE INSIGHT",
        f"Monthly charges associated with churned accounts total "
        f"{money(total_churned_charges)} in the current selection. "
        f"Active High/Critical Risk customers account for "
        f"{money(revenue_at_risk)} in monthly charges. "
        "The latter amount is exposure for prioritization, not a forecast "
        "that the full amount will be lost.",
    )

    insight(
        "FINANCIAL ACTION",
        "Prioritize retention tests by expected impact, customer count, "
        "and cost to serve. Compare campaign cost against measured "
        "incremental retention; do not treat monthly charges as profit.",
    )


# ============================================================
# PAGE 5: CUSTOMER DETAILS
# ============================================================
elif page == "Customer Details":
    section("Customer-Level Exploration")

    average_charge = (
        filtered["monthlycharges"].mean() if total else 0
    )
    average_tenure = (
        filtered["tenure"].mean()
        if "tenure" in filtered.columns and total else 0
    )

    kpi_row([
        ("Customers in View", f"{total:,}", "After page-specific filters"),
        ("Churned Customers", f"{churned_count:,}", "Churn status = yes"),
        ("Average Monthly Charge", money(average_charge), "Average charge in selection"),
        ("Average Tenure", f"{average_tenure:.1f} months", "Average months with provider"),
    ])

    left, right = st.columns(2)

    with left:
        section("Customer Status")
        status_data = pd.DataFrame({
            "Status": ["Retained", "Churned"],
            "Customers": [retained_count, churned_count],
        })
        fig = px.pie(
            status_data,
            names="Status",
            values="Customers",
            hole=0.58,
            title="Customer Status Distribution",
            color="Status",
            color_discrete_map={"Retained": GREEN, "Churned": RED},
        )
        show_chart(fig)

    with right:
        section("Customer Charges vs Tenure")
        if "tenure" in filtered.columns and total:
            fig = px.scatter(
                filtered,
                x="tenure",
                y="monthlycharges",
                color="churn",
                hover_data=["customerid", "contract"],
                title="Customer-Level Charge and Tenure",
                color_discrete_map=STATUS_COLORS,
                opacity=0.65,
            )
            show_chart(fig)
        else:
            chart_empty()

    chart_divider()
    section("Search Customers")
    search = st.text_input(
        "Search by Customer ID",
        placeholder="Type a customer ID...",
        key="customer_search",
    )

    customer_view = filtered.copy()
    if search.strip():
        customer_view = customer_view[
            customer_view["customerid"].str.contains(
                search.strip(), case=False, na=False
            )
        ]

    customer_table(
        customer_view,
        key="customer_details_table",
    )

    insight(
        "CUSTOMER EXPERIENCE INSIGHT",
        "Use customer-level records to investigate patterns, not to assume "
        "that an individual will churn. Combine the customer's tenure, "
        "contract, service usage, and charges when reviewing an account.",
    )


# ============================================================
# PAGE 6: CUSTOMER RISK & RETENTION
# ============================================================
elif page == "Customer Risk & Retention":
    section("Risk Portfolio & Retention Priorities")

    critical_count = int(critical_mask.sum())
    high_count = int(
        filtered["risk_category"].eq("High Risk").sum()
    ) if "risk_category" in filtered.columns else 0

    kpi_row([
        ("Critical Risk", f"{critical_count:,}", "Accounts in Critical Risk category", RED),
        ("High Risk", f"{high_count:,}", "Accounts in High Risk category", ORANGE),
        ("Active High/Critical", f"{active_high_count:,}", "Retained customers in high-risk categories"),
        ("Monthly Charges at Risk", money(active_high_revenue), "Monthly charges of active high-risk customers"),
    ])

    left, right = st.columns(2)

    with left:
        section("Risk Portfolio Composition")
        if "risk_category" in filtered.columns:
            risk_data = (
                filtered["risk_category"]
                .value_counts()
                .reindex(RISK_ORDER, fill_value=0)
                .rename_axis("Risk Category")
                .reset_index(name="Customers")
            )
            fig = px.pie(
                risk_data,
                names="Risk Category",
                values="Customers",
                hole=0.58,
                title="Customer Risk Mix",
                color="Risk Category",
                color_discrete_map=RISK_COLORS,
            )
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Churn Rate by Risk Category")
        result = group_churn(filtered, "risk_category")
        if not result.empty:
            result["risk_category"] = pd.Categorical(
                result["risk_category"],
                categories=RISK_ORDER,
                ordered=True,
            )
            result = result.sort_values("risk_category")
            fig = px.bar(
                result,
                x="risk_category",
                y="Churn Rate (%)",
                title="Observed Churn Rate by Risk",
                color="risk_category",
                color_discrete_map=RISK_COLORS,
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty("Risk categories are not available.")

    chart_divider()
    left, right = st.columns(2)

    with left:
        section("Risk Score vs Monthly Charges")
        if "risk_score" in filtered.columns and total:
            fig = px.scatter(
                filtered,
                x="risk_score",
                y="monthlycharges",
                color="risk_category" if "risk_category" in filtered.columns else "churn",
                hover_data=["customerid", "contract"],
                title="Risk Score and Monthly Charge",
                opacity=0.68,
                color_discrete_map=RISK_COLORS,
            )
            show_chart(fig)
        else:
            chart_empty("Risk scores are not available.")

    with right:
        section("Risk by Contract")
        if "risk_category" in filtered.columns and "contract" in filtered.columns:
            risk_contract = (
                filtered.groupby(["contract", "risk_category"], dropna=False)
                .size()
                .reset_index(name="Customers")
            )
            fig = px.bar(
                risk_contract,
                x="contract",
                y="Customers",
                color="risk_category",
                barmode="stack",
                title="Risk Composition Across Contracts",
                color_discrete_map=RISK_COLORS,
            )
            show_chart(fig)
        else:
            chart_empty()

    chart_divider()
    section("Active High-Risk Customer Queue")
    if "risk_category" in filtered.columns:
        risk_queue = filtered[
            filtered["churn"].eq("no")
            & filtered["risk_category"].isin(
                ["Critical Risk", "High Risk"]
            )
        ].copy()

        sort_columns = []
        ascending = []
        if "risk_score" in risk_queue.columns:
            sort_columns.append("risk_score")
            ascending.append(False)
        if "monthlycharges" in risk_queue.columns:
            sort_columns.append("monthlycharges")
            ascending.append(False)

        if sort_columns:
            risk_queue = risk_queue.sort_values(
                sort_columns, ascending=ascending
            )

        customer_table(
            risk_queue,
            key="active_risk_queue",
        )
    else:
        chart_empty("Risk categories are not available in the selected dataset.")

    insight(
        "RETENTION INSIGHT",
        f"There are {active_high_count:,} retained customers classified "
        f"as High or Critical Risk in this selection, associated with "
        f"{money(active_high_revenue)} in monthly charges. "
        "These customers are candidates for review, not guaranteed future churners.",
    )

    insight(
        "RETENTION ACTION",
        "Create a prioritized outreach queue, validate each customer's "
        "circumstances, and track contact, offer, response, and subsequent "
        "churn outcomes. Review the scoring rules for fairness and accuracy.",
    )


# ============================================================
# PAGE 7: RECOMMENDATIONS
# ============================================================
elif page == "Recommendations":
    section("Action Plan for Customer Retention")

    month_to_month_mask = (
        filtered["contract"].eq("Month-to-month")
        if "contract" in filtered.columns
        else pd.Series(False, index=filtered.index)
    )
    month_to_month_count = int(month_to_month_mask.sum())
    month_to_month_churn_rate = churn_rate(
        filtered[month_to_month_mask]
    )

    kpi_row([
        ("Current Churn Rate", pct(rate), "Baseline for measuring interventions", RED),
        ("Churned Customers", f"{churned_count:,}", "Observed churn in this selection"),
        ("Month-to-Month Customers", f"{month_to_month_count:,}", "Customers on flexible contracts"),
        ("Active High-Risk Customers", f"{active_high_count:,}", "Potential retention review queue"),
    ])

    section("Prioritized Recommendations")

    rec1, rec2 = st.columns(2)

    with rec1:
        insight(
            "01 · EARLY-LIFE RETENTION",
            "Review onboarding and service experience for customers "
            "in their first 12 months. Use proactive support and "
            "measure 30-, 60-, and 90-day retention outcomes.",
        )
        insight(
            "02 · CONTRACT CONVERSION",
            f"Month-to-month customers represent {month_to_month_count:,} "
            f"accounts in this selection. Their observed churn rate is "
            f"{month_to_month_churn_rate:.1f}%. Test transparent annual-plan "
            "offers without pressuring customers into unsuitable contracts.",
        )

    with rec2:
        insight(
            "03 · HIGH-VALUE RETENTION",
            "Prioritize active High/Critical Risk customers by risk score, "
            "monthly charges, tenure, and service context. Offer relevant "
            "support or plan reviews, then measure incremental impact.",
        )
        insight(
            "04 · SERVICE EXPERIENCE",
            "Investigate support, security, and service bundles alongside "
            "churn. Where data indicates a service gap, test targeted "
            "assistance and verify the result against a comparison group.",
        )

    chart_divider()
    left, right = st.columns(2)

    with left:
        section("Observed Churn by Tenure Group")
        result = group_churn(filtered, "tenure_group")
        if not result.empty:
            fig = px.bar(
                result,
                x="tenure_group",
                y="Churn Rate (%)",
                title="Tenure Groups to Review",
                color="Churn Rate (%)",
                color_continuous_scale=["#6D28D9", "#F87171"],
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    with right:
        section("Observed Churn by Contract")
        result = group_churn(filtered, "contract")
        if not result.empty:
            fig = px.bar(
                result,
                x="contract",
                y="Churn Rate (%)",
                title="Contract Groups to Review",
                color="Churn Rate (%)",
                color_continuous_scale=["#6D28D9", "#F87171"],
                hover_data=["Customers", "Churned"],
            )
            show_chart(fig)
        else:
            chart_empty()

    chart_divider()
    section("Recommended Measurement Framework")
    measurement = pd.DataFrame([
        {
            "Action": "Early-life onboarding",
            "Target": "Customers in first 12 months",
            "Success Metric": "30/60/90-day retention",
            "Guardrail": "Customer satisfaction and support burden",
        },
        {
            "Action": "Contract plan review",
            "Target": "Month-to-month customers",
            "Success Metric": "Incremental conversion and lower churn",
            "Guardrail": "Cancellation, complaints, and discount cost",
        },
        {
            "Action": "Risk-based outreach",
            "Target": "Active High/Critical Risk customers",
            "Success Metric": "Retention lift versus comparison group",
            "Guardrail": "False positives and fair treatment",
        },
        {
            "Action": "Service support",
            "Target": "Customers with service/support gaps",
            "Success Metric": "Reduced repeat contacts and churn",
            "Guardrail": "Cost to serve and resolution time",
        },
    ])
    st.dataframe(
        measurement,
        use_container_width=True,
        hide_index=True,
    )

    insight(
        "MANAGEMENT DECISION",
        "Start with a small controlled retention pilot. Define the target "
        "population, treatment, comparison group, observation period, and "
        "success metric before launch. Report retention lift and net financial "
        "impact, not only the number of customers contacted.",
    )


# ============================================================
# PROJECT INFORMATION, GITHUB AND FOOTER
# ============================================================

st.markdown("""
<style>
/* Sidebar project identity */
section[data-testid="stSidebar"] .hero-title {
    color: #DCC8FF !important;
    font-size: 1.85rem !important;
    font-weight: 950 !important;
    line-height: 1.2 !important;
    letter-spacing: 0.35px !important;
    text-shadow: 0 0 12px rgba(155, 112, 255, 0.20);
}

/* GitHub card */
.github-card {
    border: 1px solid #A985FF;
    border-radius: 10px;
    padding: 14px;
    margin: 12px 0 18px 0;
    background: rgba(155, 112, 255, 0.08);
    box-sizing: border-box;
}
.github-heading {
    color: #E2D3FF;
    font-size: 0.88rem;
    font-weight: 900;
    letter-spacing: 1.5px;
    margin-bottom: 9px;
}
.github-link {
    color: #D8C4FF !important;
    font-size: 1rem;
    font-weight: 850;
    text-decoration: none !important;
}
.github-card p {
    color: #CDBFE0;
    font-size: 0.82rem;
    line-height: 1.6;
    margin: 10px 0 0 0;
}
.github-card p a {
    color: #E0CEFF !important;
    font-weight: 750;
}

/* One clean outer frame per chart */
div[data-testid="stPlotlyChart"] {
    border: 1px solid #A985FF !important;
    border-radius: 12px !important;
    padding: 8px !important;
    margin-top: 8px !important;
    margin-bottom: 18px !important;
    background: rgba(155, 112, 255, 0.035) !important;
    box-sizing: border-box !important;
    min-width: 0 !important;
}

/* Prevent columns from forcing chart overflow */
div[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
    min-width: 0 !important;
}

/* Project information cards */
.project-info-card {
    box-sizing: border-box !important;
    width: 100% !important;
    min-height: 145px !important;
    padding: 18px !important;
    margin: 0 0 16px 0 !important;
    border: 1px solid #A985FF !important;
    border-radius: 12px !important;
    background: rgba(155, 112, 255, 0.07) !important;
}
.project-info-card h4 {
    color: #DCC8FF !important;
    font-size: 0.9rem !important;
    font-weight: 900 !important;
    letter-spacing: 1px !important;
    margin: 0 0 12px 0 !important;
}
.project-info-card p {
    color: #D5CBE3 !important;
    font-size: 0.88rem !important;
    line-height: 1.65 !important;
    margin: 0 !important;
}
.project-info-card strong {
    color: #F0E8FF !important;
}


/* === CHURN INTELLIGENCE: targeted visual refinements === */

/* Lilac sidebar title */
section[data-testid="stSidebar"] h1 {
    color: #B9A0E8 !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
}

/* One subtle frame around each chart */
div[data-testid="stPlotlyChart"] {
    border: 1px solid #D8C9F2 !important;
    border-radius: 12px !important;
    padding: 8px !important;
    box-sizing: border-box !important;
    width: 100% !important;
}

/* Keep charts within the available width */
div[data-testid="stPlotlyChart"],
div[data-testid="stPlotlyChart"] > div {
    max-width: 100% !important;
    min-width: 0 !important;
}

/* Remove bar outlines while preserving the bar fills */
div[data-testid="stPlotlyChart"] .barlayer path {
    stroke: none !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar GitHub card
st.sidebar.markdown(
    """
    <div class="github-card">
        <div class="github-heading">GITHUB</div>
        <a class="github-link"
           href="https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
           target="_blank" rel="noopener noreferrer">
            View Repository ↗
        </a>
        <p>
            If you find this project useful, please consider
            <a href="https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
               target="_blank" rel="noopener noreferrer">starring the repository</a>.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Project information appears once, at the bottom.
st.divider()
chart_divider()
section("Project Information")

project_col, author_col = st.columns(2, gap="medium")

with project_col:
    st.markdown(
        """
        <div class="project-info-card">
            <h4>PROJECT</h4>
            <p>
                <strong>Customer Churn Analytics Platform</strong><br>
                End-to-end Data Analytics &amp; Business Intelligence
                portfolio project.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with author_col:
    st.markdown(
        """
        <div class="project-info-card">
            <h4>AUTHOR</h4>
            <p>
                <strong>Aram Mehraban · 2026</strong><br>
                Data Analytics &amp; Business Intelligence Portfolio
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="project-info-card">
        <h4>BUSINESS OBJECTIVE</h4>
        <p>
            Identify churn patterns, understand customer behavior,
            measure monthly charge exposure, identify at-risk customers,
            and turn analytical insights into actionable retention strategies.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "Portfolio demonstration · USD ($) · "
    "Risk labels reflect the supplied dataset's scoring logic, "
    "not a validated production prediction model."
)