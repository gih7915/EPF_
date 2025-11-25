% rebase('layout', title='Videoaulas', nav_dict=nav_dict if 'nav_dict' in locals() else {})

<div class="welcome-section">
    <h1>🎬 Videoaulas</h1>
    <p>Assista às aulas gravadas e marque seu progresso</p>
</div>

% if aluno:
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">📚 Filtrar por Disciplina</h3>
        </div>
        <div class="card-body">
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <a href="/videoaulas?aluno_id={{aluno.id}}" 
                   class="btn{{'btn-submit' if not disciplina_selecionada else '-secondary'}}" 
                   style="text-decoration: none;">
                    Todas
                </a>
                % for disc in disciplinas_matriculadas:
                    <a href="/videoaulas?aluno_id={{aluno.id}}&disciplina_codigo={{disc.codigo}}" 
                       class="btn{{'btn-submit' if disciplina_selecionada and disciplina_selecionada.codigo == disc.codigo else '-secondary'}}"
                       style="text-decoration: none;">
                        {{disc.codigo}}
                    </a>
                % end
            </div>
            
            % if disciplina_selecionada:
                <div style="margin-top: 15px; padding: 15px; background: var(--light-gray); border-radius: 8px;">
                    <strong>{{disciplina_selecionada.codigo}} - {{disciplina_selecionada.nome}}</strong>
                    <p style="margin: 5px 0 0 0; color: var(--text-light);">
                        {{disciplina_selecionada.docente}}
                    </p>
                </div>
            % end
        </div>
    </div>
% end

% if not videos:
    <div class="card">
        <div class="card-body" style="text-align: center; padding: 40px;">
            <p style="font-size: 3em; margin-bottom: 20px;">📹</p>
            <p style="color: var(--text-light); font-size: 1.1em;">
                % if disciplina_selecionada:
                    Nenhuma videoaula disponível para esta disciplina.
                % else:
                    Nenhuma videoaula disponível. Matricule-se em disciplinas para acessar o conteúdo.
                % end
            </p>
            % if not disciplinas_matriculadas:
                <a href="/disciplinas?aluno_id={{aluno.id}}" class="btn-submit" style="text-decoration: none; display: inline-block; margin-top: 20px;">
                    Buscar Disciplinas
                </a>
            % end
        </div>
    </div>
% else:
    <div style="margin-bottom: 20px;">
        <p><strong>Total de videoaulas:</strong> {{len(videos)}}</p>
        % total_assistidas = sum(1 for v in videos if v.id in (aluno.videos_assistidos or []))
        <p><strong>Progresso:</strong> {{total_assistidas}}/{{len(videos)}} assistidas 
            <span style="color: var(--success-color);">({{int((total_assistidas/len(videos))*100) if videos else 0}}%)</span>
        </p>
    </div>
    
    % for v in videos:
        % assistido = v.id in (aluno.videos_assistidos or [])
        <div class="card" style="border-left: 4px solid {{'var(--success-color)' if assistido else 'var(--primary-color)'}};">
            <div class="card-header">
                <div style="flex: 1;">
                    <h3 class="card-title">
                        % if assistido:
                            ✅
                        % else:
                            ⏯️
                        % end
                        {{v.titulo}}
                    </h3>
                    <p style="color: var(--text-light); margin: 5px 0;">
                        {{v.disciplina or 'Geral'}}
                        % if v.duracao:
                            | ⏱ {{v.duracao}} minutos
                        % end
                    </p>
                </div>
                % if assistido:
                    <span class="badge badge-success" style="font-size: 14px;">✓ Assistido</span>
                % end
            </div>
            <div class="card-body">
                <p style="margin-bottom: 15px;">{{v.descricao or 'Sem descrição disponível'}}</p>
                
                <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                    <a href="{{v.url}}" target="_blank" class="btn-submit" style="text-decoration: none;">
                        ▶️ Assistir Vídeo
                    </a>
                    
                    % if not assistido:
                        <form method="post" action="/videoaulas/watch/{{v.id}}" style="display: inline; margin: 0;">
                            <input type="hidden" name="aluno_id" value="{{aluno.id}}">
                            <input type="hidden" name="disciplina_codigo" value="{{disciplina_selecionada.codigo if disciplina_selecionada else ''}}">
                            <button type="submit" class="btn-success" style="display: flex; align-items: center; gap: 5px;">
                                <span style="font-size: 18px;">☑️</span> Marcar como Assistido
                            </button>
                        </form>
                    % else:
                        <span style="color: var(--success-color); font-weight: 600; display: flex; align-items: center; gap: 5px;">
                            <span style="font-size: 18px;">✓</span> Concluído
                        </span>
                    % end
                </div>
            </div>
        </div>
    % end
% end

<div style="margin-top: 30px; text-align: center;">
    <a href="/dashboard/aluno" class="btn-cancel" style="text-decoration: none;">
        🏠 Voltar ao Dashboard
    </a>
</div>
