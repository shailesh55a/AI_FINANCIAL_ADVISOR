# import reportlab classes for creating PDF documents
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

# import styles for formatting text
from reportlab.lib.styles import getSampleStyleSheet

# import current date and time
from datetime import datetime

# generate financial report

def generate_pdf_report(
        income,
        expense,
        savings,
        top_category,
        ai_advice
):
    """
    Generate a financial analysis PDF.
    
    Parameters
    ----------
    income : float
    expense : float
    savings : float
    top_category : str
    ai_advice : str
    
    Returns
    -------
    
    str
        PDF file path
    """

    # create a unique file name using date & time
    finance_dir = "reports"
    finance = (
        f"{finance_dir}/Financial_Report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )
    # ensure output directory exists
    import os
    os.makedirs(finance_dir, exist_ok=True)

    # create PDF document
    # use the generated finance path as filename
    pdf = SimpleDocTemplate(finance)

    # load default reportlab styles

    styles = getSampleStyleSheet()

    # list that will store everything added to PDF

    elements = []

    # PDF Title

    elements.append(
        Paragraph(
            "<b>AI Financial Advisor Report</b>",
            styles["Title"]
        )
    )

    # add black space

    elements.append(Spacer(1, 20))

    # AI recomendations

    elements.append(
        Paragraph(
            "<b>AI Financial Recommendations</b>",
            styles.get("Heading2", styles["Title"])
        )
    )

    # replace line breaks with HTML breaks
    ai_advice = ai_advice.replace("\n", "<br/>")

    elements.append(
        Paragraph(
            ai_advice,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # footer

    elements.append(
        Paragraph(
            f"Generated on: {datetime.now()}",
            styles["Italic"]
        )
    )

    # build pdf

    pdf.build(elements)

    # return filename so app.py can offer it to download
    return finance
    