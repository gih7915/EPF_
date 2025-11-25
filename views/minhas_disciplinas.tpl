% rebase('layout', title='Minhas Disciplinas', nav_dict=nav_dict)

<div class="welcome-section">
    <h1>📖 Minhas Disciplinas</h1>
    <p>Disciplinas em que você está matriculado</p>
</div>

% if not disciplinas:
    <div class="card">
        <div class="card-body" style="text-align: center; padding: 40px;">
            <p style="font-size: 3em; margin-bottom: 20px;">📚</p>
            <p style="color: var(--text-light); font-size: 1.1em;">
                Você ainda não está matriculado em nenhuma disciplina.
            </p>
            <a href="/disciplinas?aluno_id={{aluno_id}}" class="btn-submit" style="text-decoration: none; display: inline-block; margin-top: 20px;">
                Buscar Disciplinas
            </a>
        </div>
    </div>
% else:
    <div style="margin-bottom: 20px;">
        <p><strong>Total de disciplinas:</strong> {{len(disciplinas)}}</p>
    </div>
    
    % for disc in disciplinas:
        <div class="card">
            <div class="card-header">
                <div>
                    <h3 class="card-title">{{disc.codigo}} - {{disc.nome}}</h3>
                    <p style="color: var(--text-light); margin: 5px 0;">Turma: {{disc.turma}} | {{disc.ano_periodo}}</p>
                </div>
                <span class="badge badge-success" style="font-size: 14px;">✓ Matriculado</span>
            </div>
            <div class="card-body">
                <p><strong>👨‍🏫 Professor:</strong> {{disc.docente}}</p>
                <p><strong>⏰ Horário:</strong> {{disc.horario}}</p>
                <p><strong>📍 Local:</strong> {{disc.local}}</p>
                <p><strong>🕐 Carga Horária:</strong> {{disc.carga_horaria}}</p>
                <p><strong>👥 Alunos Matriculados:</strong> {{disc.vagas_ocupadas}}/{{disc.vagas_ofertadas}}</p>
                
                <form method="post" action="/disciplinas/desmatricular/{{disc.id}}" style="margin-top: 15px;"
                      onsubmit="return confirm('Tem certeza que deseja se desmatricular desta disciplina?');">
                    <input type="hidden" name="aluno_id" value="{{aluno_id}}">
                    <button type="submit" class="btn-danger">
                        ❌ Desmatricular
                    </button>
                </form>
            </div>
        </div>
    % end
% end

<div style="margin-top: 30px; text-align: center;">
    <a href="/disciplinas?aluno_id={{aluno_id}}" class="btn-secondary" style="text-decoration: none;">
        ➕ Buscar Mais Disciplinas
    </a>
    <a href="/dashboard/aluno" class="btn-cancel" style="text-decoration: none; margin-left: 10px;">
        🏠 Voltar ao Dashboard
    </a>
</div>
