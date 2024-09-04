import streamlit as st
import pandas as pd
import plotly.express as px


# 读取Excel文件
def load_data(file):
    df = pd.read_excel(file, engine='openpyxl')
    df['Sequence_Length'] = df['Sequence'].apply(len)  # 计算序列长度
    return df


# 生成交互式图像
def generate_plot(data, group):
    filtered_data = data[data['Group'] == group].sort_values('Sequence_Length')
    fig = px.scatter(filtered_data,
                     x='Sequence_Length',
                     y='D-value',
                     hover_data=['Sequence', 'Value', 'Group', 'D-value'],
                     title=f'Plot for Group {group}')
    fig.update_layout(xaxis_title="Sequence Length", yaxis_title="D-value")
    st.plotly_chart(fig)


# 主函数
def main():
    st.title("根据Group生成交互式图像")

    uploaded_file = st.file_uploader("上传包含数据的Excel文件", type=["xlsx"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)

        # 显示Group选择器
        groups = df['Group'].unique()
        selected_group = st.selectbox("选择Group", groups)

        # 生成并显示图像
        generate_plot(df, selected_group)


if __name__ == "__main__":
    main()
