import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني موجه
G = nx.DiGraph()

# إضافة العقد (المفاهيم)
G.add_node("Programming")
G.add_node("Variables")
G.add_node("Functions")
G.add_node("Loops")

# إضافة الحواف (العلاقات) مع الأوزان
G.add_edge("Programming", "Variables", weight=1.5)
G.add_edge("Programming", "Functions", weight=2.0)
G.add_edge("Variables", "Loops", weight=1.0)
G.add_edge("Functions", "Loops", weight=2.5)

# رسم خريطة المفاهيم مع عرض الأوزان
pos = nx.spring_layout(G)  # تحديد موضع العقد
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


# 5. البحث عن المسار الأقل صعوبة من "Programming" إلى "Loops"
optimal_path = nx.shortest_path(G, source="Programming", target="Functions", weight='weight')
print("Optimal Path (Least Difficulty):", optimal_path)

# حساب التكلفة الإجمالية للمسار الأمثل
total_weight = nx.shortest_path_length(G, source="Programming", target="Functions", weight='weight')
print("Total Difficulty:", total_weight)