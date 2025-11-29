% rebase('layout', title='Disciplinas Disponíveis', nav_dict=nav_dict)

<div class="welcome-section">
    <h1>📚 Disciplinas Disponíveis</h1>
    <p>Busque e matricule-se nas disciplinas</p>
</div>

<div class="card">
    <form action="/disciplinas/buscar" method="post" style="display: flex; gap: 12px; margin-bottom: 20px;">
        <input type="hidden" name="aluno_id" value="{{aluno_id}}">
        <input type="text" name="query" placeholder="Buscar por código ou nome..." 
               value="{{query if 'query' in locals() else ''}}" 
               style="flex: 1; margin-bottom: 0;">
        <button type="submit" class="btn-submit" style="margin: 0;">🔍 Buscar</button>
        <a href="/disciplinas?aluno_id={{aluno_id}}" class="btn-secondary" style="margin: 0; text-decoration: none; display: inline-block; padding: 12px 28px;">Ver Todas</a>
    </form>
</div>

% if not disciplinas:
    <div class="card">
        <p style="text-align: center; color: var(--text-light);">Nenhuma disciplina encontrada.</p>
    </div>
% else:
    % for disc in disciplinas:
        <div class="card">
            <div class="card-header">
                <div>
                    <h3 class="card-title">{{disc.codigo}} - {{disc.nome}}</h3>
                    <p style="color: var(--text-light); margin: 5px 0;">Turma: {{disc.turma}} | {{disc.ano_periodo}}</p>
                </div>
                % if disc.id in matriculadas_ids:
                    <span class="badge badge-success" style="font-size: 14px;">✓ Matriculado</span>
                % elif not disc.tem_vagas():
                    <span class="badge badge-danger" style="font-size: 14px;">Sem Vagas</span>
                % else:
                    <span class="badge badge-info" style="font-size: 14px;">Disponível</span>
                % end
            </div>
            <div class="card-body">
                <p><strong>👨‍🏫 Professor:</strong> {{disc.docente.name}}</p>
                <p><strong>⏰ Horário:</strong> {{disc.horario}}</p>
                <p><strong>📍 Local:</strong> {{disc.local}}</p>
                <p><strong>📊 Vagas:</strong> {{disc.vagas_ocupadas}}/{{disc.vagas_ofertadas}}
                    % vagas_disponiveis = disc.vagas_ofertadas - disc.vagas_ocupadas
                    % if vagas_disponiveis > 0:
                        <span style="color: var(--success-color);">({{vagas_disponiveis}} disponíveis)</span>
                    % else:
                        <span style="color: var(--danger-color);">(Lotada)</span>
                    % end
                </p>
                <p><strong>🕐 Carga Horária:</strong> {{disc.carga_horaria}}</p>
                
                % if disc.id not in matriculadas_ids and disc.tem_vagas():
                    <div style="margin-top: 15px;">
                        <a href="/disciplinas/matricular/{{disc.id}}?aluno_id={{aluno_id}}" 
                           class="btn-submit" 
                           style="text-decoration: none; display: inline-block;">
                            ✏️ Matricular-se
                        </a>
                    </div>
                % end
            </div>
        </div>
    % end
% end

<div style="margin-top: 30px; text-align: center;">
    <a href="/disciplinas/minhas?aluno_id={{aluno_id}}" class="btn-secondary" style="text-decoration: none;">
        📖 Minhas Disciplinas
    </a>
</div>
