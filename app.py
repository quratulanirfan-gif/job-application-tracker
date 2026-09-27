import streamlit as st
import pandas as pd

from database import (
    create_database,
    add_application,
    get_applications,
    delete_application,
    update_application
)


# -------------------------
# Page configuration
# -------------------------

st.set_page_config(
    page_title="Job Application Tracker",
    layout="wide"
)


# -------------------------
# Create database
# -------------------------

create_database()


# -------------------------
# Title
# -------------------------

st.title("Job Application Tracker")

st.write(
    "Keep track of your job applications and your progress."
)


# -------------------------
# Get applications
# -------------------------

applications = get_applications()


# -------------------------
# Dashboard statistics
# -------------------------

total = len(applications)

interviews = len(
    [
        application
        for application in applications
        if application[4] == "Interview"
    ]
)

offers = len(
    [
        application
        for application in applications
        if application[4] == "Offer"
    ]
)

conversion_rate = (
    (offers / total) * 100
    if total > 0
    else 0
)


# -------------------------
# Dashboard
# -------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Applications",
    total
)

col2.metric(
    "Interviews",
    interviews
)

col3.metric(
    "Offers",
    offers
)

col4.metric(
    "Conversion Rate",
    f"{conversion_rate:.1f}%"
)

# =========================================================
# YOUR APPLICATIONS
# =========================================================

st.header("Your Applications")

applications = get_applications()

if applications:

    df = pd.DataFrame(
        applications,
        columns=[
            "ID",
            "Company",
            "Role",
            "Date Applied",
            "Status"
        ]
    )

    # -------------------------
    # Status filter
    # -------------------------

    status_filter = st.selectbox(
        "Filter by status",
        [
            "All",
            "Applied",
            "Interview",
            "Offer",
            "Rejected"
        ]
    )

    # -------------------------
    # Sort applications
    # -------------------------

    sort_option = st.selectbox(
        "Sort applications",
        [
            "Newest first",
            "Oldest first",
            "Company A-Z",
            "Company Z-A"
        ]
    )

    # -------------------------
    # Filter by status
    # -------------------------

    if status_filter != "All":

        filtered_df = df[
            df["Status"] == status_filter
        ]

    else:

        filtered_df = df

    # -------------------------
    # Sort applications
    # -------------------------

    if sort_option == "Newest first":

        filtered_df = filtered_df.sort_values(
            by="Date Applied",
            ascending=False
        )

    elif sort_option == "Oldest first":

        filtered_df = filtered_df.sort_values(
            by="Date Applied",
            ascending=True
        )

    elif sort_option == "Company A-Z":

        filtered_df = filtered_df.sort_values(
            by="Company",
            ascending=True
        )

    elif sort_option == "Company Z-A":

        filtered_df = filtered_df.sort_values(
            by="Company",
            ascending=False
        )

    # -------------------------
    # Display applications
    # -------------------------

    st.dataframe(
        filtered_df.drop(columns=["ID"]),
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No applications yet.")

# =========================================================
# ADD APPLICATION
# =========================================================

st.header("Add Application")

with st.form("application_form"):

    company = st.text_input(
        "Company",
        placeholder="e.g. Google"
    )

    role = st.text_input(
        "Role",
        placeholder="e.g. Software Developer"
    )

    date_applied = st.date_input(
        "Date Applied"
    )

    status = st.selectbox(
        "Status",
        [
            "Applied",
            "Interview",
            "Offer",
            "Rejected"
        ]
    )

    submitted = st.form_submit_button(
        "Add Application"
    )

    if submitted:

        if company.strip() and role.strip():

            add_application(
                company.strip(),
                role.strip(),
                date_applied.isoformat(),
                status
            )

            st.success(
                "Application added successfully!"
            )

            st.rerun()

        else:

            st.warning(
                "Please enter both company and role."
            )

# =========================================================
# UPDATE APPLICATION
# =========================================================

st.subheader("Update Application")

applications = get_applications()

if applications:

    df = pd.DataFrame(
        applications,
        columns=[
            "ID",
            "Company",
            "Role",
            "Date Applied",
            "Status"
        ]
    )

    # Create user-friendly names for the dropdown
    application_options = df.apply(
        lambda row: f"{row['Company']} - {row['Role']}",
        axis=1
    ).tolist()

    selected_update_application = st.selectbox(
        "Select application to update",
        application_options,
        key="update_application"
    )

    # Find the selected application
    selected_application = df[
        df.apply(
            lambda row:
            f"{row['Company']} - {row['Role']}"
            == selected_update_application,
            axis=1
        )
    ].iloc[0]

    selected_update_id = selected_application["ID"]


    with st.form("update_form"):

        new_company = st.text_input(
            "Company",
            value=selected_application["Company"]
        )

        new_role = st.text_input(
            "Role",
            value=selected_application["Role"]
        )

        new_date = st.date_input(
            "Date Applied",
            value=pd.to_datetime(
                selected_application["Date Applied"]
            ).date()
        )

        status_options = [
            "Applied",
            "Interview",
            "Offer",
            "Rejected"
        ]

        new_status = st.selectbox(
            "Status",
            status_options,
            index=status_options.index(
                selected_application["Status"]
            )
        )

        update_button = st.form_submit_button(
            "Update Application"
        )

        if update_button:

            if (
                new_company.strip()
                and new_role.strip()
            ):

                update_application(
                    selected_update_id,
                    new_company.strip(),
                    new_role.strip(),
                    new_date.isoformat(),
                    new_status
                )

                st.success(
                    "Application updated successfully!"
                )

                st.rerun()

            else:

                st.warning(
                    "Please enter both company and role."
                )

else:

    st.info(
        "No applications available to update."
    )


# =========================================================
# DELETE APPLICATION
# =========================================================

st.subheader("Delete Application")

applications = get_applications()

if applications:

    df = pd.DataFrame(
        applications,
        columns=[
            "ID",
            "Company",
            "Role",
            "Date Applied",
            "Status"
        ]
    )

    # Create user-friendly names for the dropdown
    application_options = df.apply(
        lambda row: f"{row['Company']} - {row['Role']}",
        axis=1
    ).tolist()

    selected_delete_application = st.selectbox(
        "Select application to delete",
        application_options,
        key="delete_application"
    )

    # Find the selected application
    selected_application = df[
        df.apply(
            lambda row:
            f"{row['Company']} - {row['Role']}"
            == selected_delete_application,
            axis=1
        )
    ].iloc[0]

    selected_delete_id = selected_application["ID"]

    st.write(
        f"You selected: **{selected_application['Company']} - "
        f"{selected_application['Role']}**"
    )

    confirm_delete = st.checkbox(
        "I want to delete this application"
    )

    if confirm_delete:

        if st.button(
            "Delete Selected Application"
        ):

            delete_application(
                selected_delete_id
            )

            st.success(
                "Application deleted successfully!"
            )

            st.rerun()

else:

    st.info(
        "No applications available to delete."
    )


# =========================================================
# APPLICATIONS BY STATUS
# =========================================================

st.subheader("Applications by Status")

applications = get_applications()

if applications:

    chart_df = pd.DataFrame(
        applications,
        columns=[
            "ID",
            "Company",
            "Role",
            "Date Applied",
            "Status"
        ]
    )

    status_counts = chart_df["Status"].value_counts()

    st.bar_chart(
        status_counts,
        height=100
    )

else:

    st.info(
        "No data available for the chart yet."
    )