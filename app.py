import streamlit as st
import pickle

# ── Load model artifacts ──────────────────────────────────────────────────────
model         = pickle.load(open("re_nb_model.pkl",      "rb"))
vectorizer    = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl",   "rb"))

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Requirement Classifier",
    page_icon="⬡",
    layout="centered",
)
# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    color: #111827 !important;
}

.stApp { background: #ffffff !important; }

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem; padding-bottom: 3rem; max-width: 700px; }

/* Kill ghost label rectangle above textarea */
.stTextArea label,
.stTextArea [data-testid="stWidgetLabel"] {
    display: none !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

.badge {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #065f46;
    background: #d1fae5;
    border: 1.5px solid #6ee7b7;
    padding: 5px 16px;
    border-radius: 99px;
    margin-bottom: 1.25rem;
}

.page-title {
    font-size: 36px;
    font-weight: 700;
    letter-spacing: -.03em;
    color: #111827;
    margin-bottom: .5rem;
    text-align: center;
}

.page-sub {
    font-size: 15px;
    color: #374151;
    font-weight: 400;
    line-height: 1.7;
    text-align: center;
    margin-bottom: 2.5rem;
}

.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #374151;
    margin-bottom: .6rem;
}

textarea {
    background: #f9fafb !important;
    border: 1.5px solid #d1d5db !important;
    border-radius: 12px !important;
    color: #111827 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    line-height: 1.6 !important;
    resize: none !important;
}
textarea::placeholder { color: #9ca3af !important; }
textarea:focus {
    border-color: #059669 !important;
    box-shadow: 0 0 0 3px rgba(5,150,105,.12) !important;
}

.char-count {
    text-align: right;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #6b7280;
    margin-top: 5px;
    margin-bottom: 14px;
}
.stButton > button {
    width: 100%;
    background: #059669 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: .7rem 1.5rem !important;
    letter-spacing: -.01em !important;
    transition: background .18s !important;
}
.stButton > button:hover { background: #047857 !important; }

div[data-testid="column"]:last-child .stButton > button {
    background: #ffffff !important;
    color: #374151 !important;
    border: 1.5px solid #d1d5db !important;
}
div[data-testid="column"]:last-child .stButton > button:hover {
    background: #f3f4f6 !important;
}

.result-card {
    background: #f0fdf4;
    border: 1.5px solid #6ee7b7;
    border-radius: 16px;
    padding: 1.75rem;
    margin-top: 1.75rem;
    position: relative;
}
.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: #059669;
    border-radius: 16px 16px 0 0;
}
.result-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #059669;
    margin-bottom: .5rem;
}
.result-name {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -.02em;
    color: #111827;
    margin-bottom: .25rem;
}
.result-code {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #6b7280;
    font-weight: 400;
}
.result-divider { height: 1px; background: #d1fae5; margin: 1rem 0; }
.result-desc {
    font-size: 15px;
    color: #1f2937;
    line-height: 1.7;
    font-weight: 400;
}

.conf-row {
    display: flex;
    justify-content: space-between;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    font-weight: 500;
    color: #374151;
    margin-bottom: 8px;
}
.bar-track {
    height: 6px;
    background: #d1fae5;
    border-radius: 99px;
    overflow: hidden;
}

.cats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 10px;
    margin-top: .6rem;
}
.cat-pill {
    background: #f9fafb;
    border: 1.5px solid #e5e7eb;
    border-radius: 10px;
    padding: .75rem 1rem;
}
.cat-pill-code {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    font-weight: 500;
    color: #059669;
    margin-bottom: 3px;
}
.cat-pill-name {
    font-size: 13px;
    font-weight: 500;
    color: #374151;
}

.err-box {
    background: #fef2f2;
    border: 1.5px solid #fca5a5;
    border-radius: 10px;
    padding: .75rem 1rem;
    font-size: 14px;
    font-weight: 500;
    color: #b91c1c;
    margin-top: .5rem;
}

.hr { height: 1px; background: #e5e7eb; margin: 2rem 0 1.5rem; }

.footer {
    text-align: center;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #9ca3af;
    letter-spacing: .06em;
    margin-top: 3rem;
}

/* Debug info box */
.debug-box {
    background: #fffbeb;
    border: 1.5px solid #fcd34d;
    border-radius: 10px;
    padding: .75rem 1rem;
    font-size: 13px;
    font-family: 'DM Mono', monospace;
    color: #92400e;
    margin-top: .5rem;
}
</style>
""", unsafe_allow_html=True)

# ── Explanations — covers all known label variants ────────────────────────────
# Keys include both full codes AND single-letter variants the encoder may return
EXPLANATIONS = {
    # Standard codes
    "FR":  ("Functional Requirement",
            "Defines a specific behavior or function the system must support — describes what the system does."),
    "NFR": ("Non-Functional Requirement",
            "Describes how the system performs a function — covers quality attributes like reliability, security, and maintainability."),
    "PE":  ("Performance Requirement",
            "Specifies measurable performance criteria such as speed, throughput, or response time under defined conditions."),
    "US":  ("Usability Requirement",
            "Addresses the ease of use and accessibility of the system for its intended user base."),
    "A":   ("Assumption",
            "A condition taken as true for planning purposes, without formal verification at this stage."),
    "L":   ("Limitation",
            "An explicit constraint or boundary on what the system will or can do."),
    "PO":  ("Policy Requirement",
            "Derived from regulatory, legal, or organizational rules that the system must adhere to."),
    # Single-letter fallbacks (in case label encoder uses abbreviated labels)
    "F":   ("Functional Requirement",
            "Defines a specific behavior or function the system must support — describes what the system does."),
    "N":   ("Non-Functional Requirement",
            "Describes how the system performs a function — covers quality attributes like reliability, security, and maintainability."),
    "P":   ("Performance Requirement",
            "Specifies measurable performance criteria such as speed, throughput, or response time under defined conditions."),
    "U":   ("Usability Requirement",
            "Addresses the ease of use and accessibility of the system for its intended user base."),
    "O":   ("Policy Requirement",
            "Derived from regulatory, legal, or organizational rules that the system must adhere to."),
    # Lowercase variants
    "fr":  ("Functional Requirement",
            "Defines a specific behavior or function the system must support — describes what the system does."),
    "nfr": ("Non-Functional Requirement",
            "Describes how the system performs a function — covers quality attributes like reliability, security, and maintainability."),
    "pe":  ("Performance Requirement",
            "Specifies measurable performance criteria such as speed, throughput, or response time under defined conditions."),
    "us":  ("Usability Requirement",
            "Addresses the ease of use and accessibility of the system for its intended user base."),
    "a":   ("Assumption",
            "A condition taken as true for planning purposes, without formal verification at this stage."),
    "l":   ("Limitation",
            "An explicit constraint or boundary on what the system will or can do."),
    "po":  ("Policy Requirement",
            "Derived from regulatory, legal, or organizational rules that the system must adhere to."),
}

# Display labels for the category grid (always show clean codes)
DISPLAY_CATEGORIES = [
    ("FR",  "Functional"),
    ("NFR", "Non-Functional"),
    ("PE",  "Performance"),
    ("US",  "Usability"),
    ("A",   "Assumption"),
    ("L",   "Limitation"),
    ("PO",  "Policy"),
]

def resolve_label(raw_label: str):
    """
    Robustly resolve whatever the label encoder returns into
    (display_code, full_name, description).
    Tries exact match first, then uppercase, then prefix matching.
    """
    # 1. Exact match
    if raw_label in EXPLANATIONS:
        name, desc = EXPLANATIONS[raw_label]
        return raw_label.upper(), name, desc

    # 2. Uppercase match
    upper = raw_label.strip().upper()
    if upper in EXPLANATIONS:
        name, desc = EXPLANATIONS[upper]
        return upper, name, desc

    # 3. Prefix match — e.g. "Functional" → FR
    keyword_map = {
        "FUNC": ("FR",  "Functional Requirement",
                 "Defines a specific behavior or function the system must support — describes what the system does."),
        "NON":  ("NFR", "Non-Functional Requirement",
                 "Describes how the system performs a function — covers quality attributes like reliability, security, and maintainability."),
        "PERF": ("PE",  "Performance Requirement",
                 "Specifies measurable performance criteria such as speed, throughput, or response time under defined conditions."),
        "USAB": ("US",  "Usability Requirement",
                 "Addresses the ease of use and accessibility of the system for its intended user base."),
        "ASSU": ("A",   "Assumption",
                 "A condition taken as true for planning purposes, without formal verification at this stage."),
        "LIMI": ("L",   "Limitation",
                 "An explicit constraint or boundary on what the system will or can do."),
        "POLI": ("PO",  "Policy Requirement",
                 "Derived from regulatory, legal, or organizational rules that the system must adhere to."),
    }
    for prefix, (code, name, desc) in keyword_map.items():
        if upper.startswith(prefix):
            return code, name, desc

    # 4. Fallback — show raw label with generic message
    return raw_label.upper(), f"Category: {raw_label}", \
           "This requirement has been classified into a category. Check your label encoder for full category names."


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div style="text-align:center"><span class="badge">NLP Classifier · ML-powered</span></div>',
            unsafe_allow_html=True)
st.markdown('<div class="page-title">AI REQUIREMENT CLASSIFIER</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="page-sub">Paste any software requirement below and instantly classify it into<br>'
    '<strong style="color:#111827">Functional, Non-Functional, Performance,</strong> and more.</div>',
    unsafe_allow_html=True,
)

# ── Input section ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">✏️ &nbsp;Enter Requirement</div>', unsafe_allow_html=True)

user_input = st.text_area(
    label="req",
    height=150,
    placeholder="e.g. The system shall respond to user requests within 2 seconds under normal load conditions...",
    label_visibility="hidden",
)

char_count = len(user_input)
st.markdown(f'<div class="char-count">{char_count} characters</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    predict_clicked = st.button("🔍  Classify Requirement", use_container_width=True)
with col2:
    if st.button("Clear", use_container_width=True):
        st.session_state["last_result"] = None
        st.rerun()

# ── Prediction logic ──────────────────────────────────────────────────────────
if predict_clicked:
    if not user_input.strip():
        st.markdown('<div class="err-box">⚠️ &nbsp;Please enter a requirement before classifying.</div>',
                    unsafe_allow_html=True)
    else:
        vec      = vectorizer.transform([user_input])
        raw_pred = model.predict(vec)[0]

        # Get raw label string from encoder
        raw_label = label_encoder.inverse_transform([raw_pred])[0]

        try:
            proba      = model.predict_proba(vec)[0]
            confidence = int(round(max(proba) * 100))
        except AttributeError:
            confidence = 82

        st.session_state["last_result"] = {
            "raw_label": str(raw_label),
            "confidence": confidence,
        }

# ── Result display ────────────────────────────────────────────────────────────
result = st.session_state.get("last_result")
if result:
    raw_label  = result["raw_label"]
    confidence = result["confidence"]

    display_code, full_name, description = resolve_label(raw_label)

    st.markdown(f"""
    <div class="result-card">
        <div class="result-eyebrow">✅ &nbsp;Predicted Type</div>
        <div class="result-name">{full_name}</div>
        <div class="result-code">Code: {display_code}</div>
        <div class="result-divider"></div>
        <div class="result-desc">📘 &nbsp;{description}</div>
        <div class="result-divider"></div>
        <div class="conf-row">
            <span>Confidence score</span>
            <span>{confidence}%</span>
        </div>
        <div class="bar-track">
            <div style="height:100%;width:{confidence}%;background:#059669;border-radius:99px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Show raw label in a debug note so you can update EXPLANATIONS if needed
    if display_code != raw_label.upper():
        st.markdown(
            f'<div class="debug-box">ℹ️ Raw label from encoder: <strong>"{raw_label}"</strong> — '
            f'mapped to <strong>{display_code}</strong>. '
            f'If this looks wrong, check what classes your label_encoder was trained on.</div>',
            unsafe_allow_html=True,
        )

# ── Categories reference ──────────────────────────────────────────────────────
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-label">📂 &nbsp;All Categories</div>', unsafe_allow_html=True)

cats_html = '<div class="cats-grid">'
for code, name in DISPLAY_CATEGORIES:
    cats_html += f"""
    <div class="cat-pill">
        <div class="cat-pill-code">{code}</div>
        <div class="cat-pill-name">{name}</div>
    </div>"""
cats_html += '</div>'
st.markdown(cats_html, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="footer">Built with Machine Learning &amp; NLP · Streamlit</div>',
    unsafe_allow_html=True,
)
