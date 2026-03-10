# ============================================================
# 🏃 CardioFit Treadmill Dashboard — FULLY FUNCTIONAL
# SDG 3: Good Health and Well-Being
# Paste this entire cell into Google Colab and run it.
# ============================================================

from IPython.display import display, HTML

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CardioFit – Treadmill Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>
<style>
:root {
  --red:#E8341C; --dark:#0D0D0D; --card:#161616; --card2:#1E1E1E;
  --border:#2A2A2A; --text:#F0EDE8; --muted:#777; --green:#27C97A;
  --amber:#F5A623; --blue:#4A9EFF;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html,body{background:var(--dark);color:var(--text);font-family:'DM Sans',sans-serif;min-height:100vh;}

/* HEADER */
header{display:flex;align-items:center;justify-content:space-between;padding:16px 24px;border-bottom:1px solid var(--border);background:#0D0D0D;position:sticky;top:0;z-index:100;}
.logo{font-family:'Bebas Neue',sans-serif;font-size:1.9rem;letter-spacing:3px;color:var(--red);}
.sdg-badge{display:flex;align-items:center;gap:8px;background:#0d1a0d;border:1px solid #27C97A44;border-radius:40px;padding:6px 16px;font-size:0.72rem;color:var(--green);font-weight:600;letter-spacing:1px;}

/* NAV */
.nav{display:flex;gap:4px;padding:16px 24px 0;border-bottom:1px solid var(--border);background:var(--dark);}
.nav-btn{padding:10px 20px;border-radius:8px 8px 0 0;border:1px solid var(--border);border-bottom:none;background:var(--card);color:var(--muted);font-family:'DM Sans',sans-serif;font-size:0.88rem;font-weight:500;cursor:pointer;transition:all .2s;}
.nav-btn.active{background:var(--card2);color:var(--text);border-color:var(--border);border-bottom:1px solid var(--card2);margin-bottom:-1px;}
.nav-btn:hover:not(.active){color:var(--text);}

/* MAIN */
main{padding:24px;max-width:1060px;margin:0 auto;}
.tab-content{display:none;animation:fadeIn .3s ease;}
.tab-content.active{display:block;}
@keyframes fadeIn{from{opacity:0;transform:translateY(5px);}to{opacity:1;transform:none;}}

/* LEVEL SELECTOR */
.level-row{display:flex;gap:12px;margin-bottom:24px;flex-wrap:wrap;}
.level-card{flex:1;min-width:150px;border-radius:14px;padding:18px 16px;border:2px solid var(--border);background:var(--card);cursor:pointer;transition:all .2s;text-align:center;}
.level-card:hover{transform:translateY(-2px);}
.level-card.selected{background:var(--card2);}
.level-card.easy.selected{border-color:var(--green);}
.level-card.medium.selected{border-color:var(--amber);}
.level-card.hard.selected{border-color:var(--red);}
.level-card.easy.selected .level-name{color:var(--green);}
.level-card.medium.selected .level-name{color:var(--amber);}
.level-card.hard.selected .level-name{color:var(--red);}
.level-emoji{font-size:1.8rem;margin-bottom:6px;}
.level-name{font-family:'Bebas Neue',sans-serif;font-size:1.25rem;letter-spacing:2px;color:var(--muted);}
.level-sub{font-size:0.74rem;color:var(--muted);margin-top:3px;line-height:1.4;}

/* CARDS */
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:22px;margin-bottom:18px;}
.card h2{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;letter-spacing:2px;margin-bottom:14px;display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
.tag{display:inline-block;padding:3px 10px;border-radius:20px;font-size:0.68rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;}
.tag.green{background:#27C97A22;color:var(--green);}
.tag.amber{background:#F5A62322;color:var(--amber);}
.tag.red{background:#E8341C22;color:var(--red);}
.tag.blue{background:#4A9EFF22;color:var(--blue);}

/* WORKOUT STEPS */
.step-table{width:100%;border-collapse:collapse;font-size:0.84rem;}
.step-table th{text-align:left;color:var(--muted);font-weight:600;letter-spacing:1px;text-transform:uppercase;font-size:0.68rem;padding:8px 10px;border-bottom:1px solid var(--border);}
.step-table td{padding:9px 10px;border-bottom:1px solid #1c1c1c;vertical-align:middle;}
.step-table tr:last-child td{border-bottom:none;}
.step-table tr.active-step td{background:#1f1408;}
.phase-pill{display:inline-block;padding:3px 10px;border-radius:20px;font-size:0.68rem;font-weight:700;}
.phase-warmup{background:#4A9EFF22;color:var(--blue);}
.phase-main{background:#E8341C22;color:var(--red);}
.phase-cooldown{background:#27C97A22;color:var(--green);}

/* TIMER */
.timer-box{background:var(--card2);border:1px solid var(--border);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;align-items:center;gap:14px;}
.timer-display{font-family:'Space Mono',monospace;font-size:4rem;color:var(--red);letter-spacing:8px;transition:color .3s;}
.timer-display.running{color:#ff6b4a;}
.timer-phase{font-size:0.8rem;color:var(--muted);letter-spacing:2px;text-transform:uppercase;min-height:20px;}
.timer-progress-wrap{width:100%;max-width:340px;}
.timer-progress-bg{background:var(--border);border-radius:4px;height:6px;overflow:hidden;margin-top:4px;}
.timer-progress-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--red),#ff8c5a);transition:width .5s linear;}
.btn-row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;}
.btn{padding:10px 22px;border-radius:10px;font-family:'DM Sans',sans-serif;font-size:0.88rem;font-weight:600;cursor:pointer;border:none;transition:all .15s;display:inline-flex;align-items:center;gap:6px;}
.btn:active{transform:scale(0.97);}
.btn-primary{background:var(--red);color:#fff;}
.btn-primary:hover{background:#c02a16;}
.btn-secondary{background:var(--card);color:var(--text);border:1px solid var(--border);}
.btn-secondary:hover{background:var(--border);}
.btn-success{background:var(--green);color:#000;}
.btn-success:hover{background:#1fa362;}
.btn-amber{background:var(--amber);color:#000;}
.btn-amber:hover{background:#d4901e;}

/* EDUCATION */
.edu-info{background:var(--card2);border:1px solid var(--border);border-radius:14px;padding:22px;margin-bottom:18px;line-height:1.8;font-size:0.88rem;color:#ccc;}
.edu-info p{margin-bottom:12px;}
.edu-info p:last-child{margin-bottom:0;}
.edu-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;}
.edu-card{background:var(--card2);border:1px solid var(--border);border-radius:14px;padding:18px;}
.edu-card .icon{font-size:1.8rem;margin-bottom:8px;}
.edu-card h3{font-size:0.95rem;font-weight:600;margin-bottom:6px;}
.edu-card p{font-size:0.8rem;color:#999;line-height:1.6;}

/* FORM */
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;}
.form-group{display:flex;flex-direction:column;gap:5px;}
.form-group label{font-size:0.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px;}
.form-group input,.form-group select{background:var(--card2);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:10px 12px;font-family:'DM Sans',sans-serif;font-size:0.88rem;outline:none;transition:border-color .2s;width:100%;}
.form-group input:focus,.form-group select:focus{border-color:var(--red);}
select option{background:var(--dark);}

/* TRACKER */
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:18px;}
.stat-box{background:var(--card2);border:1px solid var(--border);border-radius:14px;padding:16px 18px;}
.stat-val{font-family:'Bebas Neue',sans-serif;font-size:2rem;color:var(--red);}
.stat-lbl{font-size:0.7rem;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-top:2px;}
.log-table{width:100%;border-collapse:collapse;font-size:0.82rem;}
.log-table th{text-align:left;color:var(--muted);font-size:0.68rem;text-transform:uppercase;letter-spacing:1px;padding:8px 10px;border-bottom:1px solid var(--border);}
.log-table td{padding:9px 10px;border-bottom:1px solid #1a1a1a;vertical-align:middle;}
.log-table tr:hover td{background:#1a1a1a;}
.empty-state{text-align:center;padding:36px;color:var(--muted);font-size:0.88rem;}
.empty-state .big{font-size:2.5rem;margin-bottom:10px;}
.week-bar-bg{background:var(--border);border-radius:4px;height:10px;overflow:hidden;margin-top:6px;}
.week-bar-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--red),#ff6b4a);transition:width .6s ease;}
.streak-dots{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;}
.dot{width:30px;height:30px;border-radius:50%;border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:0.65rem;color:var(--muted);}
.dot.done{background:var(--red);border-color:var(--red);color:#fff;}
.dot.today-empty{border-color:var(--amber);color:var(--amber);}

/* SDG BOX */
.sdg-box{background:linear-gradient(135deg,#0d1a10,#081410);border:1px solid #27C97A44;border-radius:14px;padding:18px 22px;margin-bottom:20px;display:flex;gap:14px;align-items:flex-start;}
.sdg-box h3{font-family:'Bebas Neue',sans-serif;font-size:1.1rem;letter-spacing:2px;color:var(--green);margin-bottom:5px;}
.sdg-box p{font-size:0.8rem;color:#999;line-height:1.6;}

/* ALERT */
.alert{padding:10px 16px;border-radius:10px;font-size:0.83rem;margin-bottom:14px;display:none;}
.alert.success{background:#0d1f11;border:1px solid #27C97A55;color:var(--green);}
.alert.info{background:#0d1220;border:1px solid #4A9EFF44;color:var(--blue);}
.delete-btn{background:none;border:none;color:var(--muted);cursor:pointer;font-size:1rem;padding:2px 6px;border-radius:4px;transition:color .15s;}
.delete-btn:hover{color:var(--red);}
::-webkit-scrollbar{width:5px;}::-webkit-scrollbar-track{background:#111;}::-webkit-scrollbar-thumb{background:#333;border-radius:3px;}
</style>
</head>
<body>

<header>
  <div class="logo">CardioFit 🏃</div>
  <div class="sdg-badge">🌍 SDG 3 · Good Health &amp; Well-Being</div>
</header>

<div class="nav">
  <button class="nav-btn active" onclick="switchTab('workout',this)">🏋️ Workout</button>
  <button class="nav-btn"        onclick="switchTab('education',this)">📚 Education</button>
  <button class="nav-btn"        onclick="switchTab('tracker',this)">📊 My Tracker</button>
</div>

<main>

<!-- ══════════════ TAB: WORKOUT ══════════════ -->
<div class="tab-content active" id="tab-workout">

  <div class="sdg-box">
    <div style="font-size:2.2rem;flex-shrink:0">💚</div>
    <div>
      <h3>UN Sustainable Development Goal 3</h3>
      <p>This app supports <strong style="color:var(--text)">SDG 3: Good Health and Well-Being</strong>. Cardiovascular disease is the world's #1 killer — responsible for 17.9 million deaths a year. Regular treadmill exercise is one of the most powerful and accessible ways to fight back.</p>
    </div>
  </div>

  <!-- LEVEL SELECTOR -->
  <p style="font-size:0.72rem;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">Choose Your Level</p>
  <div class="level-row">
    <div class="level-card easy selected" id="wl-easy" onclick="selectWorkoutLevel('easy')">
      <div class="level-emoji">🟢</div>
      <div class="level-name">Easy</div>
      <div class="level-sub">30 min · 120 BPM · Walking/Light Jog</div>
    </div>
    <div class="level-card medium" id="wl-medium" onclick="selectWorkoutLevel('medium')">
      <div class="level-emoji">🟡</div>
      <div class="level-name">Medium</div>
      <div class="level-sub">35 min · 140 BPM · Brisk Run Intervals</div>
    </div>
    <div class="level-card hard" id="wl-hard" onclick="selectWorkoutLevel('hard')">
      <div class="level-emoji">🔴</div>
      <div class="level-name">Hard</div>
      <div class="level-sub">40 min · 165 BPM · HIIT Sprints</div>
    </div>
  </div>

  <!-- WORKOUT PLAN TABLE -->
  <div class="card" id="workoutPlanCard">
    <h2 id="planTitle">📋 Today's Easy Session <span class="tag green">60% MAX HR · 120 BPM</span></h2>
    <p id="planSubtitle" style="font-size:0.83rem;color:#999;margin-bottom:16px;line-height:1.6;"></p>
    <div style="overflow-x:auto;">
      <table class="step-table">
        <thead><tr>
          <th>#</th><th>Phase</th><th>Duration</th><th>Speed</th><th>Incline</th><th>Target HR</th><th>Instruction</th>
        </tr></thead>
        <tbody id="stepTableBody"></tbody>
      </table>
    </div>
  </div>

  <!-- TIMER -->
  <div class="card">
    <h2>⏱️ Live Session Timer</h2>
    <div class="timer-box">
      <div class="timer-phase" id="timerPhaseLabel">Press START to begin your session</div>
      <div class="timer-display" id="timerDisplay">00:00</div>
      <div class="timer-progress-wrap">
        <div style="display:flex;justify-content:space-between;font-size:0.72rem;color:var(--muted);">
          <span>Elapsed</span><span id="timerTotalLabel">/ 30:00</span>
        </div>
        <div class="timer-progress-bg"><div class="timer-progress-fill" id="timerFill" style="width:0%"></div></div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="startBtn" onclick="startTimer()">▶ Start</button>
        <button class="btn btn-secondary" onclick="pauseTimer()">⏸ Pause</button>
        <button class="btn btn-secondary" onclick="resetTimer()">↺ Reset</button>
      </div>
      <div id="timerDoneMsg" style="display:none;text-align:center;color:var(--green);font-weight:600;font-size:1rem;">🎉 Session Complete! Don't forget to log your workout below.</div>
    </div>
  </div>

  <!-- LOG WORKOUT -->
  <div class="card">
    <h2>✅ Log This Workout</h2>
    <div id="logSuccessAlert" class="alert success">✓ Workout saved! Head to the Tracker tab to see your progress.</div>
    <div class="form-grid">
      <div class="form-group">
        <label>Date</label>
        <input type="date" id="logDate"/>
      </div>
      <div class="form-group">
        <label>Level Completed</label>
        <select id="logLevel">
          <option value="Easy">🟢 Easy</option>
          <option value="Medium">🟡 Medium</option>
          <option value="Hard">🔴 Hard</option>
        </select>
      </div>
      <div class="form-group">
        <label>Duration (minutes)</label>
        <input type="number" id="logDuration" placeholder="e.g. 30" min="1" max="180"/>
      </div>
      <div class="form-group">
        <label>Distance (km) – optional</label>
        <input type="number" id="logDistance" placeholder="e.g. 3.5" step="0.1" min="0"/>
      </div>
      <div class="form-group">
        <label>How did you feel?</label>
        <select id="logMood">
          <option>😊 Great</option>
          <option>😐 Okay</option>
          <option>😅 Tough but done it</option>
          <option>💪 Beast mode</option>
          <option>😓 Struggled today</option>
        </select>
      </div>
      <div class="form-group">
        <label>Notes (optional)</label>
        <input type="text" id="logNotes" placeholder="How was your session?"/>
      </div>
    </div>
    <button class="btn btn-success" onclick="logWorkout()">💾 Add Workout to Tracker</button>
  </div>

</div>

<!-- ══════════════ TAB: EDUCATION ══════════════ -->
<div class="tab-content" id="tab-education">

  <p style="font-size:0.72rem;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;">Select Level to Learn More</p>
  <div class="level-row">
    <div class="level-card easy selected" id="el-easy" onclick="selectEduLevel('easy')">
      <div class="level-emoji">🟢</div>
      <div class="level-name">Easy</div>
      <div class="level-sub">Cardiovascular health basics</div>
    </div>
    <div class="level-card medium" id="el-medium" onclick="selectEduLevel('medium')">
      <div class="level-emoji">🟡</div>
      <div class="level-name">Medium</div>
      <div class="level-sub">Muscle groups &amp; why they matter</div>
    </div>
    <div class="level-card hard" id="el-hard" onclick="selectEduLevel('hard')">
      <div class="level-emoji">🔴</div>
      <div class="level-name">Hard</div>
      <div class="level-sub">Advanced physiology &amp; HIIT science</div>
    </div>
  </div>

  <div id="eduContent"></div>

</div>

<!-- ══════════════ TAB: TRACKER ══════════════ -->
<div class="tab-content" id="tab-tracker">

  <div class="stats-row">
    <div class="stat-box"><div class="stat-val" id="statTotal">0</div><div class="stat-lbl">Total Workouts</div></div>
    <div class="stat-box"><div class="stat-val" id="statMins">0</div><div class="stat-lbl">Minutes Trained</div></div>
    <div class="stat-box"><div class="stat-val" id="statKm">0.0</div><div class="stat-lbl">Kilometres Run</div></div>
    <div class="stat-box"><div class="stat-val" id="statWeek">0</div><div class="stat-lbl">Sessions This Week</div></div>
  </div>

  <div class="card">
    <h2>🎯 Weekly Goal — WHO Recommendation</h2>
    <p style="font-size:0.82rem;color:#999;margin-bottom:12px;">The World Health Organisation recommends at least <strong style="color:var(--text)">150 minutes</strong> of moderate cardiovascular activity per week. Here's your progress:</p>
    <div style="font-size:0.82rem;color:var(--muted);margin-bottom:4px;" id="weekProgressLabel">0 / 150 min</div>
    <div class="week-bar-bg"><div class="week-bar-fill" id="weekBarFill" style="width:0%"></div></div>
    <div style="margin-top:16px;">
      <div style="font-size:0.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Last 7 Days Activity</div>
      <div class="streak-dots" id="streakDots"></div>
    </div>
  </div>

  <div class="card">
    <h2>📜 Workout Log</h2>
    <div id="workoutLog"></div>
    <div style="margin-top:14px;">
      <button class="btn btn-secondary" onclick="clearLog()" style="font-size:0.8rem;padding:8px 16px;">🗑 Clear All Logs</button>
    </div>
  </div>

</div>
</main>

<script>
// ═══════════════════════════════
// DATA: Workout Plans
// ═══════════════════════════════
const PLANS = {
  easy: {
    title:'📋 Easy Session',
    badge:'60% MAX HR · 120 BPM',
    badgeClass:'green',
    totalMins: 30,
    subtitle:'This session targets 60% of your maximum heart rate — approximately 120 beats per minute. At this intensity you should be able to hold a full conversation. Use this zone to build your cardiovascular base without overexerting yourself. Walk or light jog — whatever keeps you at that steady 120 BPM.',
    steps:[
      {phase:'Warm-Up',   dur:'5 min',  sec:300,  speed:'3.0 – 4.0 km/h', incline:'0%',  hr:'~100 BPM', note:'Slow easy walk. Deep breaths. Swing arms naturally.'},
      {phase:'Main',      dur:'10 min', sec:600,  speed:'4.5 – 5.5 km/h', incline:'0%',  hr:'~115 BPM', note:'Brisk walk. Keep posture upright. Core lightly engaged.'},
      {phase:'Main',      dur:'10 min', sec:600,  speed:'5.0 – 6.0 km/h', incline:'1%',  hr:'~120 BPM', note:'Target zone reached. Slight incline. Breathe rhythmically.'},
      {phase:'Main',      dur:'5 min',  sec:300,  speed:'4.5 km/h',        incline:'0%',  hr:'~118 BPM', note:'Maintain steady pace. Focus on even, relaxed breathing.'},
      {phase:'Cool-Down', dur:'5 min',  sec:300,  speed:'3.0 km/h',        incline:'0%',  hr:'~100 BPM', note:'Slow gentle walk. Let heart rate fall naturally.'},
    ]
  },
  medium: {
    title:'📋 Medium Session',
    badge:'70% MAX HR · 140 BPM',
    badgeClass:'amber',
    totalMins: 35,
    subtitle:'This session targets 70% of your maximum heart rate — approximately 140 beats per minute. You will be working harder; able to speak only in short sentences. This zone burns more fat and builds greater cardiovascular endurance through run/walk intervals.',
    steps:[
      {phase:'Warm-Up',   dur:'5 min',  sec:300,  speed:'5.0 km/h',        incline:'0%',  hr:'~110 BPM', note:'Brisk warm-up walk. Gradually increase pace.'},
      {phase:'Main',      dur:'5 min',  sec:300,  speed:'8.0 – 9.0 km/h',  incline:'0%',  hr:'~135 BPM', note:'Easy jog. Land mid-foot, relax shoulders.'},
      {phase:'Main',      dur:'2 min',  sec:120,  speed:'5.5 km/h',         incline:'2%',  hr:'~125 BPM', note:'Active recovery walk. Incline keeps intensity up.'},
      {phase:'Main',      dur:'5 min',  sec:300,  speed:'9.0 – 10.0 km/h', incline:'0%',  hr:'~140 BPM', note:'Target zone. Controlled effort. Focus on breathing.'},
      {phase:'Main',      dur:'2 min',  sec:120,  speed:'5.5 km/h',         incline:'2%',  hr:'~125 BPM', note:'Recovery. Keep moving — do NOT stop.'},
      {phase:'Main',      dur:'5 min',  sec:300,  speed:'9.5 km/h',         incline:'1%',  hr:'~142 BPM', note:'Push back to target zone. Strong, consistent effort.'},
      {phase:'Main',      dur:'5 min',  sec:300,  speed:'9.0 km/h',         incline:'0%',  hr:'~138 BPM', note:'Maintain. You are building real cardiovascular fitness here.'},
      {phase:'Cool-Down', dur:'6 min',  sec:360,  speed:'4.0 km/h',         incline:'0%',  hr:'~110 BPM', note:'Walk it out slowly. Deep belly breaths.'},
    ]
  },
  hard: {
    title:'📋 Hard Session — HIIT',
    badge:'85%+ MAX HR · 165 BPM',
    badgeClass:'red',
    totalMins: 40,
    subtitle:'Advanced high-intensity interval training (HIIT). You will push to 85%+ of your max heart rate during sprint intervals, then recover, and go again. This maximises cardiovascular output, increases VO2 max, and creates an afterburn effect that elevates your metabolism for hours. Only attempt if you have a solid cardio base.',
    steps:[
      {phase:'Warm-Up',   dur:'5 min',  sec:300,  speed:'6.0 – 7.0 km/h',  incline:'0%',  hr:'~120 BPM', note:'Progressive jog. Build heat before the hard work.'},
      {phase:'Main',      dur:'1 min',  sec:60,   speed:'13.0 – 15.0 km/h', incline:'0%',  hr:'~170 BPM', note:'ALL-OUT SPRINT. Maximum controlled effort. Drive arms!'},
      {phase:'Main',      dur:'2 min',  sec:120,  speed:'6.5 km/h',          incline:'0%',  hr:'~130 BPM', note:'Active recovery jog. Do not stop. Breathe deep.'},
      {phase:'Main',      dur:'1 min',  sec:60,   speed:'13.0 km/h',          incline:'2%',  hr:'~172 BPM', note:'Sprint + incline. Explosive power through the hill.'},
      {phase:'Main',      dur:'2 min',  sec:120,  speed:'6.5 km/h',           incline:'0%',  hr:'~128 BPM', note:'Recovery. Get your breath back for the next push.'},
      {phase:'Main',      dur:'1 min',  sec:60,   speed:'14.0 km/h',          incline:'0%',  hr:'~175 BPM', note:'Sprint repeat. Mental toughness time. Push through!'},
      {phase:'Main',      dur:'2 min',  sec:120,  speed:'6.5 km/h',           incline:'0%',  hr:'~130 BPM', note:'Recovery. Last sprint coming up.'},
      {phase:'Main',      dur:'1 min',  sec:60,   speed:'14.0 – 16.0 km/h',  incline:'0%',  hr:'~178 BPM', note:'FINAL SPRINT. Leave it all on the belt!'},
      {phase:'Main',      dur:'3 min',  sec:180,  speed:'5.5 km/h',           incline:'3%',  hr:'~140 BPM', note:'Incline power walk. Glutes firing. Controlled breathing.'},
      {phase:'Cool-Down', dur:'5 min',  sec:300,  speed:'4.0 km/h',           incline:'0%',  hr:'~110 BPM', note:'Slow walk down. You earned this. Breathe it all out.'},
    ]
  }
};

// ═══════════════════════════════
// DATA: Education Content
// ═══════════════════════════════
const EDU = {
  easy: `
    <div class="card">
      <h2>❤️ Cardiovascular Health &amp; Treadmill Exercise <span class="tag green">BEGINNER</span></h2>
      <div class="edu-info">
        <p>Regular aerobic exercise such as walking and running strengthens the heart and improves the efficiency of the cardiovascular system. These activities increase heart rate and oxygen use, training the heart muscle to pump blood more effectively and improving circulation throughout the body. Over time, this leads to a lower resting heart rate, improved blood vessel function, and reduced blood pressure.</p>
        <p>Walking and running also help regulate important cardiovascular risk factors. Research shows that regular physical activity can lower cholesterol levels, reduce the risk of hypertension, improve blood sugar control, and decrease the likelihood of heart disease and stroke.</p>
        <p>Both activities provide strong protective effects against cardiovascular disease. Studies show that even 5–10 minutes of running per day can significantly reduce the risk of death from cardiovascular causes, while regular walking is associated with dose-dependent reductions in heart disease risk.</p>
        <p>In simple terms, consistent walking or running trains the heart, improves blood flow, and reduces long-term cardiovascular risk — making them two of the most effective and accessible ways to maintain heart health.</p>
      </div>
      <div class="edu-grid">
        <div class="edu-card"><div class="icon">🫀</div><h3>Stronger Heart</h3><p>Regular walking strengthens the heart muscle so it pumps more blood with less effort — leading to a lower resting heart rate over time.</p></div>
        <div class="edu-card"><div class="icon">🫁</div><h3>Better Lungs</h3><p>Cardio trains your lungs to use oxygen more efficiently, reducing breathlessness during everyday activities like climbing stairs.</p></div>
        <div class="edu-card"><div class="icon">🧠</div><h3>Mental Health</h3><p>Exercise releases endorphins — natural mood-lifters. Even a 20-minute walk reduces stress, anxiety, and symptoms of depression.</p></div>
        <div class="edu-card"><div class="icon">🩸</div><h3>Lower Blood Pressure</h3><p>Consistent cardio reduces blood pressure naturally — one of the biggest risk factors for heart attack and stroke.</p></div>
        <div class="edu-card"><div class="icon">⚖️</div><h3>Weight Management</h3><p>Regular walking burns calories and improves metabolism, helping regulate body weight even hours after exercise.</p></div>
        <div class="edu-card"><div class="icon">😴</div><h3>Better Sleep</h3><p>People who exercise regularly fall asleep faster, sleep more deeply, and wake feeling more rested and energised.</p></div>
      </div>
    </div>`,
  medium: `
    <div class="card">
      <h2>💪 Muscles Worked &amp; Why It Matters <span class="tag amber">INTERMEDIATE</span></h2>
      <div class="edu-info">
        <p>Treadmill running and brisk walking are full lower-body compound movements that simultaneously train your cardiovascular system and major muscle groups. When you understand which muscles are working and why, you can train smarter, recover better, and see faster results.</p>
        <p>At moderate intensity (70% max heart rate), your body enters a sustained aerobic state. Your muscles require a steady oxygen supply, which forces your heart and lungs to work harder and adapt over time. This is where real cardiovascular improvement happens.</p>
        <p>Incline walking or running dramatically increases glute and hamstring activation while keeping your heart rate elevated — making it one of the most efficient ways to combine strength and cardio training simultaneously.</p>
      </div>
      <div class="edu-grid">
        <div class="edu-card"><div class="icon">🦵</div><h3>Quadriceps</h3><p><strong style="color:var(--amber)">Primary.</strong> Extend the knee with every stride. Stronger quads improve speed and reduce knee injury risk.</p></div>
        <div class="edu-card"><div class="icon">🦵</div><h3>Hamstrings</h3><p><strong style="color:var(--amber)">Primary.</strong> Drive the leg back and control the forward swing. Critical for stride power and injury prevention.</p></div>
        <div class="edu-card"><div class="icon">🍑</div><h3>Glutes</h3><p><strong style="color:var(--amber)">Primary on incline.</strong> Power every push-off. Incline treadmill dramatically increases glute activation.</p></div>
        <div class="edu-card"><div class="icon">🦶</div><h3>Calves</h3><p>Propel you forward with each toe-off. Running conditions calves for better ankle stability and lower-leg endurance.</p></div>
        <div class="edu-card"><div class="icon">🏋️</div><h3>Core</h3><p>Stabilises your torso throughout each stride. A strong core improves running efficiency and protects your spine.</p></div>
        <div class="edu-card"><div class="icon">🫀</div><h3>Heart</h3><p>The most important muscle. Every cardio session makes your heart pump more powerfully and efficiently — permanently.</p></div>
      </div>
    </div>`,
  hard: `
    <div class="card">
      <h2>⚡ Advanced Physiology: HIIT Science <span class="tag red">ADVANCED</span></h2>
      <div class="edu-info">
        <p>At high intensity, you enter anaerobic zones — your body can't get enough oxygen to fuel muscles purely aerobically, so it supplements with fast-burning glycogen stores. This creates an "oxygen debt" repaid after exercise, called EPOC (Excess Post-Exercise Oxygen Consumption) — meaning you burn more calories for up to 24 hours post-workout.</p>
        <p>Sprint intervals are the single most effective training method for improving VO2 max — your body's maximum oxygen-use capacity and the strongest single predictor of long-term cardiovascular health and longevity. Just 3 HIIT sessions per week have been shown to improve VO2 max by 10–15% within 8 weeks.</p>
        <p>HIIT also dramatically improves insulin sensitivity — your muscles absorb blood sugar more efficiently, reducing type 2 diabetes risk by up to 58%. The intense effort also spikes BDNF (Brain-Derived Neurotrophic Factor), a protein that grows new brain cells and acts as a powerful natural antidepressant.</p>
      </div>
      <div class="edu-grid">
        <div class="edu-card"><div class="icon">📈</div><h3>VO2 Max</h3><p>Max oxygen your body can use. HIIT is the most effective way to increase it — the strongest predictor of cardiovascular longevity.</p></div>
        <div class="edu-card"><div class="icon">🔥</div><h3>EPOC / Afterburn</h3><p>After intense intervals, metabolism stays elevated for 12–24 hours — you keep burning calories long after you step off the treadmill.</p></div>
        <div class="edu-card"><div class="icon">🧬</div><h3>Mitochondria</h3><p>Sprint training increases mitochondria density in muscle cells — dramatically improving energy production and fatigue resistance.</p></div>
        <div class="edu-card"><div class="icon">🩺</div><h3>Cardiac Remodelling</h3><p>Intense cardio enlarges heart chambers (athlete's heart), allowing more blood pumped per beat — the highest cardiovascular adaptation.</p></div>
        <div class="edu-card"><div class="icon">⚖️</div><h3>Insulin Sensitivity</h3><p>HIIT is exceptionally powerful at reducing blood sugar and protecting against type 2 diabetes — even a single session has measurable effects.</p></div>
        <div class="edu-card"><div class="icon">🧠</div><h3>BDNF</h3><p>Intense exercise spikes Brain-Derived Neurotrophic Factor — grows new brain cells, sharpens memory, and acts as a natural antidepressant.</p></div>
      </div>
    </div>`
};

// ═══════════════════════════════
// APP STATE
// ═══════════════════════════════
let currentLevel = 'easy';
let timerSec = 0;
let timerRunning = false;
let timerInterval = null;
let currentStepIndex = 0;
let workouts = JSON.parse(localStorage.getItem('cardiofit_v2') || '[]');

// ═══════════════════════════════
// INIT
// ═══════════════════════════════
window.onload = () => {
  document.getElementById('logDate').value = new Date().toISOString().split('T')[0];
  renderWorkoutPlan('easy');
  renderEduContent('easy');
  renderTracker();
};

// ═══════════════════════════════
// TABS
// ═══════════════════════════════
function switchTab(tab, btn) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + tab).classList.add('active');
  btn.classList.add('active');
  if (tab === 'tracker') renderTracker();
}

// ═══════════════════════════════
// WORKOUT PLAN
// ═══════════════════════════════
function selectWorkoutLevel(level) {
  currentLevel = level;
  ['easy','medium','hard'].forEach(l => {
    const el = document.getElementById('wl-' + l);
    el.classList.remove('selected');
  });
  document.getElementById('wl-' + level).classList.add('selected');
  document.getElementById('logLevel').value = level.charAt(0).toUpperCase() + level.slice(1);
  renderWorkoutPlan(level);
  resetTimer();
}

function renderWorkoutPlan(level) {
  const p = PLANS[level];
  document.getElementById('planTitle').innerHTML = p.title + ' <span class="tag ' + p.badgeClass + '">' + p.badge + '</span>';
  document.getElementById('planSubtitle').textContent = p.subtitle;
  document.getElementById('timerTotalLabel').textContent = '/ ' + String(p.totalMins).padStart(2,'0') + ':00';
  const tbody = document.getElementById('stepTableBody');
  tbody.innerHTML = '';
  p.steps.forEach((s, i) => {
    const phClass = s.phase.includes('Warm') ? 'phase-warmup' : s.phase.includes('Cool') ? 'phase-cooldown' : 'phase-main';
    tbody.innerHTML += `<tr id="step-row-${i}">
      <td style="color:var(--muted);font-family:'Space Mono',monospace">${i+1}</td>
      <td><span class="phase-pill ${phClass}">${s.phase}</span></td>
      <td style="font-family:'Space Mono',monospace;white-space:nowrap">${s.dur}</td>
      <td style="color:var(--amber);font-family:'Space Mono',monospace;white-space:nowrap">${s.speed}</td>
      <td style="color:var(--blue);font-family:'Space Mono',monospace">${s.incline}</td>
      <td style="color:var(--red);font-family:'Space Mono',monospace;white-space:nowrap">${s.hr}</td>
      <td style="color:#bbb;font-size:0.8rem">${s.note}</td>
    </tr>`;
  });
}

// ═══════════════════════════════
// TIMER (FULLY FUNCTIONAL)
// ═══════════════════════════════
function startTimer() {
  if (timerRunning) return;
  timerRunning = true;
  document.getElementById('timerDisplay').classList.add('running');
  document.getElementById('startBtn').style.opacity = '0.5';
  timerInterval = setInterval(() => {
    timerSec++;
    updateTimerDisplay();
    updateTimerProgress();
    updateActiveStep();
    // Check if done
    const totalSec = PLANS[currentLevel].totalMins * 60;
    if (timerSec >= totalSec) {
      clearInterval(timerInterval);
      timerRunning = false;
      document.getElementById('timerDoneMsg').style.display = 'block';
      document.getElementById('timerPhaseLabel').textContent = '✅ SESSION COMPLETE!';
      document.getElementById('startBtn').style.opacity = '1';
      // Auto-fill duration
      document.getElementById('logDuration').value = PLANS[currentLevel].totalMins;
    }
  }, 1000);
}

function pauseTimer() {
  if (!timerRunning) return;
  timerRunning = false;
  clearInterval(timerInterval);
  document.getElementById('timerDisplay').classList.remove('running');
  document.getElementById('timerPhaseLabel').textContent = '⏸ Paused — press Start to continue';
  document.getElementById('startBtn').style.opacity = '1';
}

function resetTimer() {
  pauseTimer();
  timerSec = 0;
  currentStepIndex = 0;
  document.getElementById('timerDisplay').textContent = '00:00';
  document.getElementById('timerDisplay').classList.remove('running');
  document.getElementById('timerPhaseLabel').textContent = 'Press START to begin your session';
  document.getElementById('timerFill').style.width = '0%';
  document.getElementById('timerDoneMsg').style.display = 'none';
  document.getElementById('startBtn').style.opacity = '1';
  // Remove highlights
  const rows = document.querySelectorAll('.step-table tbody tr');
  rows.forEach(r => r.classList.remove('active-step'));
}

function updateTimerDisplay() {
  const m = String(Math.floor(timerSec / 60)).padStart(2, '0');
  const s = String(timerSec % 60).padStart(2, '0');
  document.getElementById('timerDisplay').textContent = m + ':' + s;
}

function updateTimerProgress() {
  const totalSec = PLANS[currentLevel].totalMins * 60;
  const pct = Math.min(100, (timerSec / totalSec) * 100);
  document.getElementById('timerFill').style.width = pct + '%';
}

function updateActiveStep() {
  const steps = PLANS[currentLevel].steps;
  let elapsed = 0;
  let activeIdx = steps.length - 1;
  for (let i = 0; i < steps.length; i++) {
    if (timerSec < elapsed + steps[i].sec) { activeIdx = i; break; }
    elapsed += steps[i].sec;
  }
  if (activeIdx !== currentStepIndex) {
    const oldRow = document.getElementById('step-row-' + currentStepIndex);
    if (oldRow) oldRow.classList.remove('active-step');
    currentStepIndex = activeIdx;
  }
  const activeRow = document.getElementById('step-row-' + activeIdx);
  if (activeRow) {
    activeRow.classList.add('active-step');
    document.getElementById('timerPhaseLabel').textContent =
      'Step ' + (activeIdx + 1) + ' of ' + steps.length + ' · ' + steps[activeIdx].phase + ' · ' + steps[activeIdx].hr;
  }
}

// ═══════════════════════════════
// LOG WORKOUT
// ═══════════════════════════════
function logWorkout() {
  const date     = document.getElementById('logDate').value;
  const level    = document.getElementById('logLevel').value;
  const duration = parseInt(document.getElementById('logDuration').value) || 0;
  const distance = parseFloat(document.getElementById('logDistance').value) || 0;
  const mood     = document.getElementById('logMood').value;
  const notes    = document.getElementById('logNotes').value.trim();

  if (!date) { alert('Please select a date.'); return; }
  if (!duration || duration < 1) { alert('Please enter how many minutes you trained.'); return; }

  workouts.unshift({ id: Date.now(), date, level, duration, distance, mood, notes });
  localStorage.setItem('cardiofit_v2', JSON.stringify(workouts));

  // Clear fields
  document.getElementById('logDuration').value = '';
  document.getElementById('logDistance').value = '';
  document.getElementById('logNotes').value = '';

  // Show success
  const alert = document.getElementById('logSuccessAlert');
  alert.style.display = 'block';
  setTimeout(() => alert.style.display = 'none', 4000);
}

// ═══════════════════════════════
// EDUCATION
// ═══════════════════════════════
function selectEduLevel(level) {
  ['easy','medium','hard'].forEach(l => document.getElementById('el-' + l).classList.remove('selected'));
  document.getElementById('el-' + level).classList.add('selected');
  renderEduContent(level);
}

function renderEduContent(level) {
  document.getElementById('eduContent').innerHTML = EDU[level];
}

// ═══════════════════════════════
// TRACKER
// ═══════════════════════════════
function renderTracker() {
  const total = workouts.length;
  const mins  = workouts.reduce((a, w) => a + w.duration, 0);
  const km    = workouts.reduce((a, w) => a + w.distance, 0);

  const now = new Date();
  const startOfWeek = new Date(now);
  startOfWeek.setDate(now.getDate() - now.getDay());
  startOfWeek.setHours(0,0,0,0);
  const thisWeek = workouts.filter(w => new Date(w.date) >= startOfWeek);
  const weekMins = thisWeek.reduce((a, w) => a + w.duration, 0);

  document.getElementById('statTotal').textContent = total;
  document.getElementById('statMins').textContent  = mins;
  document.getElementById('statKm').textContent    = km.toFixed(1);
  document.getElementById('statWeek').textContent  = thisWeek.length;

  const pct = Math.min(100, Math.round((weekMins / 150) * 100));
  document.getElementById('weekBarFill').style.width = pct + '%';
  document.getElementById('weekProgressLabel').textContent =
    weekMins + ' / 150 min this week (' + pct + '% of WHO goal' + (pct >= 100 ? ' ✅ GOAL MET!' : '') + ')';

  renderStreakDots();
  renderLogTable();
}

function renderStreakDots() {
  const container = document.getElementById('streakDots');
  container.innerHTML = '';
  const today = new Date();
  const days = ['Su','Mo','Tu','We','Th','Fr','Sa'];
  for (let i = 6; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(today.getDate() - i);
    const dStr = d.toISOString().split('T')[0];
    const done = workouts.some(w => w.date === dStr);
    const isToday = i === 0;
    const label = days[d.getDay()];
    const wrap = document.createElement('div');
    wrap.style.cssText = 'text-align:center;display:flex;flex-direction:column;align-items:center;gap:3px;';
    wrap.innerHTML = `<div class="dot ${done?'done':isToday?'today-empty':''}">${done?'✓':label}</div>
      <div style="font-size:0.58rem;color:var(--muted)">${label}</div>`;
    container.appendChild(wrap);
  }
}

function renderLogTable() {
  const container = document.getElementById('workoutLog');
  if (!workouts.length) {
    container.innerHTML = '<div class="empty-state"><div class="big">🏃</div><p>No workouts logged yet.<br>Complete a session on the <strong>Workout</strong> tab and hit <strong>Add Workout to Tracker</strong>.</p></div>';
    return;
  }
  const levelColor = {Easy:'var(--green)', Medium:'var(--amber)', Hard:'var(--red)'};
  let html = `<div style="overflow-x:auto"><table class="log-table">
    <thead><tr><th>Date</th><th>Level</th><th>Duration</th><th>Distance</th><th>Mood</th><th>Notes</th><th></th></tr></thead><tbody>`;
  workouts.forEach((w, i) => {
    const c = levelColor[w.level] || 'var(--text)';
    html += `<tr>
      <td style="font-family:'Space Mono',monospace;font-size:0.8rem">${w.date}</td>
      <td><strong style="color:${c}">${w.level}</strong></td>
      <td>${w.duration} min</td>
      <td>${w.distance ? w.distance + ' km' : '—'}</td>
      <td>${w.mood}</td>
      <td style="color:var(--muted);font-size:0.78rem">${w.notes || '—'}</td>
      <td><button class="delete-btn" onclick="deleteWorkout(${i})" title="Delete">✕</button></td>
    </tr>`;
  });
  html += '</tbody></table></div>';
  container.innerHTML = html;
}

function deleteWorkout(idx) {
  if (confirm('Remove this workout from your log?')) {
    workouts.splice(idx, 1);
    localStorage.setItem('cardiofit_v2', JSON.stringify(workouts));
    renderTracker();
  }
}

function clearLog() {
  if (confirm('Clear ALL workout history? This cannot be undone.')) {
    workouts = [];
    localStorage.removeItem('cardiofit_v2');
    renderTracker();
  }
}
</script>
</body>
</html>
"""

display(HTML(html_code))
