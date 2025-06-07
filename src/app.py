import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import from data module
from data.students_data import get_dataframe, get_subjects, get_summary_stats

# Configure page
st.set_page_config(
    page_title="BCA Student Performance Analysis",
    page_icon="📊",
    layout="wide"
)

def main():
    st.title("🎓 Academic Performance Analysis")
    st.markdown("---")
    
    # Sidebar for controls
    st.sidebar.header("📋 Analysis Controls")
    num_students = st.sidebar.slider("Number of Students", 20, 100, 50)
    
    # Generate data
    df = get_dataframe(num_students)
    subjects = get_subjects()
    stats = get_summary_stats(df)
    
    # Display summary metrics
    st.header("📈 Key Performance Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", stats['total_students'])
    with col2:
        st.metric("Pass Rate", f"{stats['pass_rate']}%")
    with col3:
        st.metric("Average Percentage", f"{stats['average_percentage']}%")
    with col4:
        st.metric("Top Performer", stats['highest_scorer'])
    
    # Data overview
    st.header("📋 Student Data Overview")
    if st.checkbox("Show Raw Data"):
        st.dataframe(df, use_container_width=True)
    
    # Charts section
    st.header("📊 Performance Analysis Charts")
    
    # Create tabs for different chart categories
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Distribution Analysis", "📊 Comparative Analysis", "🎯 Individual Performance", "📉 Statistical Analysis"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Grade distribution pie chart
            st.subheader("Grade Distribution")
            grade_counts = df['grade'].value_counts()
            fig_pie = px.pie(
                values=grade_counts.values,
                names=grade_counts.index,
                title="Student Grade Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Pass/Fail status
            st.subheader("Pass/Fail Status")
            status_counts = df['status'].value_counts()
            fig_status = px.bar(
                x=status_counts.index,
                y=status_counts.values,
                title="Pass/Fail Distribution",
                color=status_counts.index,
                color_discrete_map={'Pass': 'green', 'Fail': 'red'}
            )
            st.plotly_chart(fig_status, use_container_width=True)
        
        # Percentage distribution histogram
        st.subheader("Percentage Score Distribution")
        fig_hist = px.histogram(
            df, 
            x='percentage', 
            nbins=20, 
            title="Distribution of Student Percentages",
            color_discrete_sequence=['skyblue']
        )
        fig_hist.add_vline(x=df['percentage'].mean(), line_dash="dash", line_color="red", 
                          annotation_text=f"Mean: {df['percentage'].mean():.1f}%")
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with tab2:
        # Subject-wise performance comparison
        st.subheader("Subject-wise Performance Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Box plot for subject scores - FIXED
            subject_data = df[subjects].melt(var_name='Subject', value_name='Score')
            fig_box = px.box(
                subject_data, 
                x='Subject', 
                y='Score',
                title="Score Distribution by Subject",
                color='Subject'
            )
            # Fixed: Use update_layout instead of update_xaxis
            fig_box.update_layout(xaxis_tickangle=45)
            st.plotly_chart(fig_box, use_container_width=True)
        
        with col2:
            # Average scores by subject
            avg_scores = df[subjects].mean().sort_values(ascending=True)
            fig_bar = px.bar(
                x=avg_scores.values,
                y=avg_scores.index,
                orientation='h',
                title="Average Scores by Subject",
                color=avg_scores.values,
                color_continuous_scale='viridis'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Correlation heatmap
        st.subheader("Subject Correlation Analysis")
        correlation_matrix = df[subjects].corr()
        fig_heatmap = px.imshow(
            correlation_matrix,
            title="Subject Score Correlations",
            color_continuous_scale='RdBu',
            aspect='auto'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with tab3:
        # Individual student performance
        st.subheader("Individual Student Performance Analysis")
        
        # Student selector
        selected_students = st.multiselect(
            "Select Students to Compare",
            df['name'].tolist(),
            default=df['name'].head(5).tolist()
        )
        
        if selected_students:
            selected_df = df[df['name'].isin(selected_students)]
            
            # Radar chart for selected students
            fig_radar = go.Figure()
            
            for _, student in selected_df.iterrows():
                fig_radar.add_trace(go.Scatterpolar(
                    r=[student[subject] for subject in subjects],
                    theta=subjects,
                    fill='toself',
                    name=student['name']
                ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True,
                title="Student Performance Radar Chart"
            )
            st.plotly_chart(fig_radar, use_container_width=True)
            
            # Performance comparison table
            st.subheader("Selected Students Comparison")
            comparison_df = selected_df[['name', 'percentage', 'grade', 'status'] + subjects]
            st.dataframe(comparison_df, use_container_width=True)
    
    with tab4:
        # Statistical analysis
        st.subheader("Statistical Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Attendance vs Performance scatter plot
            st.subheader("Attendance vs Performance")
            fig_scatter = px.scatter(
                df, 
                x='attendance', 
                y='percentage',
                color='grade',
                title="Attendance vs Academic Performance",
                hover_data=['name']
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Semester-wise performance
            st.subheader("Semester-wise Performance")
            semester_avg = df.groupby('semester')['percentage'].mean().reset_index()
            fig_semester = px.line(
                semester_avg, 
                x='semester', 
                y='percentage',
                title="Average Performance by Semester",
                markers=True
            )
            st.plotly_chart(fig_semester, use_container_width=True)
        
        # Additional charts in tab4
        st.subheader("Performance Distribution by Grade")
        col3, col4 = st.columns(2)
        
        with col3:
            # Violin plot for grade-wise score distribution
            grade_data = df[['grade', 'percentage']].copy()
            fig_violin = px.violin(
                grade_data,
                x='grade',
                y='percentage',
                title="Percentage Distribution by Grade",
                box=True
            )
            st.plotly_chart(fig_violin, use_container_width=True)
        
        with col4:
            # Subject difficulty analysis
            subject_difficulty = df[subjects].std().sort_values(ascending=False)
            fig_difficulty = px.bar(
                x=subject_difficulty.values,
                y=subject_difficulty.index,
                orientation='h',
                title="Subject Difficulty (Standard Deviation)",
                color=subject_difficulty.values,
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_difficulty, use_container_width=True)
        
        # Statistical summary
        st.subheader("Statistical Summary")
        st.write("**Overall Statistics:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write(f"**Mean Percentage:** {df['percentage'].mean():.2f}%")
            st.write(f"**Median Percentage:** {df['percentage'].median():.2f}%")
            st.write(f"**Standard Deviation:** {df['percentage'].std():.2f}")
        
        with col2:
            st.write(f"**Highest Score:** {df['percentage'].max():.2f}%")
            st.write(f"**Lowest Score:** {df['percentage'].min():.2f}%")
            st.write(f"**Range:** {df['percentage'].max() - df['percentage'].min():.2f}")
        
        with col3:
            st.write(f"**Students Above 80%:** {(df['percentage'] >= 80).sum()}")
            st.write(f"**Students Below 50%:** {(df['percentage'] < 50).sum()}")
            st.write(f"**Average Attendance:** {df['attendance'].mean():.1f}%")
        
        # Subject-wise statistics table
        st.subheader("Subject-wise Performance Statistics")
        subject_stats = pd.DataFrame({
            'Subject': subjects,
            'Mean': [df[subject].mean() for subject in subjects],
            'Median': [df[subject].median() for subject in subjects],
            'Std Dev': [df[subject].std() for subject in subjects],
            'Min': [df[subject].min() for subject in subjects],
            'Max': [df[subject].max() for subject in subjects],
            'Pass Rate (≥35)': [(df[subject] >= 35).sum() / len(df) * 100 for subject in subjects]
        })
        subject_stats = subject_stats.round(2)
        st.dataframe(subject_stats, use_container_width=True)

    # Additional insights section
    st.header("🔍 Key Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Performance Insights")
        
        # Top 5 performers
        top_performers = df.nlargest(5, 'percentage')[['name', 'percentage', 'grade']]
        st.write("**Top 5 Performers:**")
        for i, row in top_performers.iterrows():
            st.write(f"🏆 {row['name']}: {row['percentage']}% ({row['grade']})")
        
        # Subject with highest average
        best_subject = df[subjects].mean().idxmax()
        best_avg = df[subjects].mean().max()
        st.write(f"**Best Performing Subject:** {best_subject} ({best_avg:.1f}%)")
        
    with col2:
        st.subheader("⚠️ Areas for Improvement")
        
        # Bottom 5 performers
        bottom_performers = df.nsmallest(5, 'percentage')[['name', 'percentage', 'grade']]
        st.write("**Students Needing Support:**")
        for i, row in bottom_performers.iterrows():
            st.write(f"📚 {row['name']}: {row['percentage']}% ({row['grade']})")
        
        # Subject with lowest average
        weak_subject = df[subjects].mean().idxmin()
        weak_avg = df[subjects].mean().min()
        st.write(f"**Most Challenging Subject:** {weak_subject} ({weak_avg:.1f}%)")

    # Footer
    st.markdown("---")
    st.markdown("**📊 BCA Student Performance Analysis Dashboard** | Built with Streamlit & Plotly")

if __name__ == "__main__":
    main()