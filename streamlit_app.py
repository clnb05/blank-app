import streamlit as st
import pandas as pd
import plotly.express as px


# 读取Excel文件
def load_data(file):
    df = pd.read_excel(file, engine='openpyxl')
    df['Sequence_Length'] = df['Sequence'].apply(len)  # 计算序列长度（如果需要，可以保留这列）
    return df


# 生成交互式图像
def generate_plot(data, group):
    # 过滤出选定的 group 数据
    filtered_data = data[data['Group'] == group].sort_values('Value')  # 按 Value 排序
    # 绘制图像，将 x 轴改为 Value
    fig = px.scatter(filtered_data,
                     x='Value',  # 将横坐标设为 Value
                     y='D-value',  # 纵坐标仍然是 D-value
                     hover_data=['Sequence', 'Value', 'Group', 'D-value'],  # 显示更多数据
                     title=f'Plot for Group {group}')
    # 设置图像的标题和轴标签
    fig.update_layout(xaxis_title="Retention Time (Value)", yaxis_title="D-value")
    # 显示图像
    st.plotly_chart(fig)


# 主函数
def main():
    st.title("根据Group生成交互式图像")

    # 上传 Excel 文件
    uploaded_file = st.file_uploader("上传包含数据的Excel文件", type=["xlsx"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)

        # 显示 Group 选择器
        groups = df['Group'].unique()
        selected_group = st.selectbox("选择Group", groups)

        # 生成并显示图像
        generate_plot(df, selected_group)


if __name__ == "__main__":
    main()
