
from flask import Flask, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt

# إنشاء رسم بياني
G = nx.Graph()

# إضافة العقد (التخصصات)
G.add_nodes_from(["Frontend", "Backend", "Mobile Development", "HTML", "CSS", "JavaScript", "Database Management", "Server-Side Languages", "Mobile Frameworks", "Cross-Platform Development"])

# إضافة الحواف مع الأوزان (التي تعكس العلاقة بين التخصصات)
G.add_edge("Frontend", "HTML", weight=1)
G.add_edge("Frontend", "CSS", weight=1)
G.add_edge("Frontend", "JavaScript", weight=1)
G.add_edge("Backend", "Database Management", weight=1)
G.add_edge("Backend", "Server-Side Languages", weight=1)
G.add_edge("Mobile Development", "Mobile Frameworks", weight=1)
G.add_edge("Mobile Development", "Cross-Platform Development", weight=1)

# تصور الرسم البياني
nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.show()

app = Flask(__name__)

# بناء الرسم البياني
G = nx.Graph()
G.add_nodes_from(["Frontend", "Backend", "Mobile Development", "HTML", "CSS", "JavaScript", "Database Management", "Server-Side Languages", "Mobile Frameworks", "Cross-Platform Development"])
G.add_edge("Frontend", "HTML", weight=1)
G.add_edge("Frontend", "CSS", weight=1)
G.add_edge("Frontend", "JavaScript", weight=1)
G.add_edge("Backend", "Database Management", weight=1)
G.add_edge("Backend", "Server-Side Languages", weight=1)
G.add_edge("Mobile Development", "Mobile Frameworks", weight=1)
G.add_edge("Mobile Development", "Cross-Platform Development", weight=1)

def recommend_specialization(answers):
    scores = {"Frontend": 0, "Backend": 0, "Mobile Development": 0}

    if answers.get('interest_in_ui', 'no') == 'yes':
        scores["Frontend"] += 1
    if answers.get('experience_with_databases', 'no') == 'yes':
        scores["Backend"] += 1
    if answers.get('interest_in_mobile_apps', 'no') == 'yes':
        scores["Mobile Development"] += 1

    # تحديد التخصص الأعلى درجة
    recommended_specialization = max(scores, key=scores.get)
    return recommended_specialization

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    answers = data.get('answers', {})
    recommendation = recommend_specialization(answers)
    return jsonify({'recommended_specialization': recommendation})

if __name__ == 'main':
    app.run(debug=True)