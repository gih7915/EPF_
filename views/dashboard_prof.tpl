% rebase('layout', title='Dashboard do Professor', nav_dict=nav_dict)

<div class="welcome-section">
    <h1>Bem-vindo(a), Prof. {{prof.name}}! 👨‍🏫</h1>
    <p>Painel de Gestão Acadêmica</p>
</div>

<div class="dashboard-grid">
    <a href="/lancar_notas" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📝</div>
        <h2 class="dashboard-title">Lançar Notas</h2>
        <p class="dashboard-description">Registre e gerencie as notas dos alunos por disciplina e avaliação.</p>
    </a>

    <a href="/lancar_faltas" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📋</div>
        <h2 class="dashboard-title">Registrar Faltas</h2>
        <p class="dashboard-description">Faça o controle de presença e ausências dos seus alunos.</p>
    </a>

    <a href="/criar_atividade" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📚</div>
        <h2 class="dashboard-title">Criar Atividades</h2>
        <p class="dashboard-description">Crie tarefas, trabalhos e exercícios para suas turmas.</p>
    </a>

    <a href="/perfil_professor?prof_id={{prof.id}}" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">👤</div>
        <h2 class="dashboard-title">Meu Perfil</h2>
        <p class="dashboard-description">Gerencie suas informações pessoais.</p>
    </a>

    <a href="/postar_videoaula" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">🎥</div>
        <h2 class="dashboard-title">Postar Videoaulas</h2>
        <p class="dashboard-description">Compartilhe aulas gravadas e materiais de apoio com os alunos.</p>
    </a>

    <a href="/enviar_recado" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">💬</div>
        <h2 class="dashboard-title">Enviar Recados</h2>
        <p class="dashboard-description">Comunique-se com alunos através de avisos e mensagens importantes.</p>
    </a>

    <a href="/visualizar_turmas" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">👥</div>
        <h2 class="dashboard-title">Minhas Turmas</h2>
        <p class="dashboard-description">Visualize as turmas sob sua responsabilidade e informações dos alunos.</p>
    </a>

    <a href="/avaliar_trabalhos" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">✅</div>
        <h2 class="dashboard-title">Avaliar Trabalhos</h2>
        <p class="dashboard-description">Corrija e avalie os trabalhos submetidos pelos alunos.</p>
    </a>

    <a href="/relatorios" class="dashboard-card" style="text-decoration: none; color: inherit;">
        <div class="dashboard-icon">📊</div>
        <h2 class="dashboard-title">Relatórios</h2>
        <p class="dashboard-description">Gere relatórios de desempenho, frequência e estatísticas das turmas.</p>
    </a>

    
</div>

<div class="card">
    <div class="card-header">
        <h3 class="card-title">Informações do Professor</h3>
    </div>
    <div class="card-body">
        <p><strong>Cargo:</strong> {{prof.cargo or 'Professor'}}</p>
        <p><strong>Email:</strong> {{prof.email}}</p>
        <p><strong>Status:</strong> <span class="badge badge-success">Ativo</span></p>
    </div>
</div>
