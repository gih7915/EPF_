% rebase('layout', title='Dashboard do Aluno', nav_dict=nav_dict)

<div class="welcome-section">
    <h1>Bem-vindo(a), {{aluno.name}}! 📚</h1>
    <p>Seu painel de estudante</p>
</div>

<div class="dashboard-grid">
    <a href="/disciplinas?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📚</div>
        <h2 class="dashboard-title">Disciplinas</h2>
        <p class="dashboard-description">Busque, matricule-se e gerencie suas disciplinas do semestre.</p>
    </a>

    <a href="/videoaulas?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">🎬</div>
        <h2 class="dashboard-title">Videoaulas</h2>
        <p class="dashboard-description">Acesse as aulas gravadas, assista e acompanhe seu progresso de aprendizado.</p>
    </a>

    <a href="/minhas_notas?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📊</div>
        <h2 class="dashboard-title">Minhas Notas</h2>
        <p class="dashboard-description">Visualize suas notas por disciplina e acompanhe seu desempenho acadêmico.</p>
    </a>

    <a href="/minhas_faltas?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📅</div>
        <h2 class="dashboard-title">Controle de Faltas</h2>
        <p class="dashboard-description">Verifique suas faltas por disciplina e fique atento à sua frequência.</p>
    </a>

    <a href="/tarefas?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📝</div>
        <h2 class="dashboard-title">Atividades</h2>
        <p class="dashboard-description">Veja suas tarefas pendentes, submeta trabalhos e acompanhe prazos.</p>
    </a>

    <a href="/meu_perfil?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">👤</div>
        <h2 class="dashboard-title">Meu Perfil</h2>
        <p class="dashboard-description">Gerencie suas informações pessoais e preferências do sistema.</p>
    </a>

    <a href="/recados?aluno_id={{aluno.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">💬</div>
        <h2 class="dashboard-title">Recados</h2>
        <p class="dashboard-description">Leia mensagens e avisos importantes dos seus professores.</p>
    </a>
</div>

<div class="card">
    <div class="card-header">
        <h3 class="card-title">Informações do Curso</h3>
    </div>
    <div class="card-body">
        <p><strong>Curso:</strong> {{aluno.curso or 'Não informado'}}</p>
        <p><strong>Matrícula:</strong> {{aluno.matricula or 'Não informado'}}</p>
        <p><strong>Status:</strong> <span class="badge badge-success">Ativo</span></p>
    </div>
</div>
