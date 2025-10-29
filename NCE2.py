import pandas as pd
from collections import defaultdict

# --- 参数设定 ---

# 1. 总课文数
TOTAL_LESSONS = 96

# 2. 艾宾浩斯遗忘曲线复习节点（单位：天）
# 表示在学习新课文后的第1, 2, 4, 7, 15, 30天后需要复习
REVIEW_OFFSETS = [1, 2, 4, 7, 15, 30]

# 3. 学习进度：每天学习一篇新课文
LESSONS_PER_DAY = 1

# 4. 输出文件名
OUTPUT_FILENAME = "nce2_memorization_plan.xlsx"

# --- 程序主体 ---

def create_memorization_plan():
    """
    生成新概念2册96篇课文的艾宾浩斯背诵计划
    """
    
    # 计算总共需要多少天
    # 需要的天数 = 学完所有课文的天数 + 最后一个复习周期
    total_learning_days = TOTAL_LESSONS // LESSONS_PER_DAY
    if TOTAL_LESSONS % LESSONS_PER_DAY != 0:
        total_learning_days += 1
        
    total_plan_days = total_learning_days + max(REVIEW_OFFSETS)
    
    print(f"总课文数: {TOTAL_LESSONS} 篇")
    print(f"复习周期: 学习后的第 {', '.join(map(str, REVIEW_OFFSETS))} 天")
    print(f"学习进度: {LESSONS_PER_DAY} 篇新课文 / 天")
    print(f"计划总天数: {total_plan_days} 天")
    
    # 使用字典来存储每天的任务
    # 结构: { day_number: {"new": [], "review": []} }
    tasks_by_day = defaultdict(lambda: {"new": [], "review": []})
    
    current_lesson = 1
    
    # 遍历计划中的每一天
    for day in range(1, total_plan_days + 1):
        
        # 1. 分配新课文任务
        if current_lesson <= TOTAL_LESSONS:
            for _ in range(LESSONS_PER_DAY):
                if current_lesson <= TOTAL_LESSONS:
                    tasks_by_day[day]["new"].append(f"Lesson {current_lesson}")
                    
                    # 2. 为这篇新课文安排未来的复习任务
                    for offset in REVIEW_OFFSETS:
                        review_day = day + offset
                        if review_day <= total_plan_days:
                            tasks_by_day[review_day]["review"].append(f"Lesson {current_lesson}")
                    
                    current_lesson += 1

    # 3. 格式化数据以便写入Excel
    plan_data = []
    for day in range(1, total_plan_days + 1):
        tasks = tasks_by_day[day]
        
        # 格式化新课文
        new_task = "无" if not tasks["new"] else ", ".join(tasks["new"])
        
        # 格式化复习课文，并排序
        review_list = sorted(tasks["review"], key=lambda x: int(x.split(" ")[1]))
        review_task = "无" if not review_list else ", ".join(review_list)
        
        plan_data.append({
            "第几天": day,
            "背诵新课文": new_task,
            "复习旧课文": review_task
        })
        
    # 4. 创建DataFrame并保存到Excel
    df = pd.DataFrame(plan_data)
    
    try:
        # 使用 openpyxl 引擎来更好地设置列宽
        with pd.ExcelWriter(OUTPUT_FILENAME, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='背诵计划')
            
            # 自动调整列宽
            worksheet = writer.sheets['背诵计划']
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter # 获取列字母
                if column_letter == 'A': # 第几天
                    max_length = 8
                elif column_letter == 'B': # 新课文
                    max_length = 20
                elif column_letter == 'C': # 复习课文
                    max_length = 50 # 给复习列更宽的空间
                
                worksheet.column_dimensions[column_letter].width = max_length

        print(f"\n成功！已生成艾宾浩斯背诵计划表: {OUTPUT_FILENAME}")
        
    except Exception as e:
        print(f"\n错误：无法写入Excel文件。请确保关闭 {OUTPUT_FILENAME} 文件后再运行。")
        print(f"详细错误: {e}")

# --- 运行程序 ---
if __name__ == "__main__":
    create_memorization_plan()