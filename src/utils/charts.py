import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def plot_bar_chart(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(data['Student'], data['Score'], color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_pie_chart(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data['Score'], labels=data['Student'], autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

def plot_line_graph(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Student'], data['Score'], marker='o', linestyle='-', color='orange')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Streamlit-compatible chart functions
def create_streamlit_bar_chart(data, x_col, y_col, title):
    """Create a Plotly bar chart for Streamlit"""
    fig = px.bar(data, x=x_col, y=y_col, title=title)
    return fig

def create_streamlit_pie_chart(values, names, title):
    """Create a Plotly pie chart for Streamlit"""
    fig = px.pie(values=values, names=names, title=title)
    return fig

def create_streamlit_line_chart(data, x_col, y_col, title):
    """Create a Plotly line chart for Streamlit"""
    fig = px.line(data, x=x_col, y=y_col, title=title, markers=True)
    return fig

def create_streamlit_scatter_plot(data, x_col, y_col, color_col, title):
    """Create a Plotly scatter plot for Streamlit"""
    fig = px.scatter(data, x=x_col, y=y_col, color=color_col, title=title)
    return fig

def create_streamlit_heatmap(data, title):
    """Create a Plotly heatmap for Streamlit"""
    fig = px.imshow(data, title=title, color_continuous_scale='viridis')
    return fig