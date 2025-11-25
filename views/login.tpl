% rebase('layout', title='Login', nav_dict={})

<section class="form-section">
    <h1>🔐 Acesse sua conta</h1>
    <h3>Entre com suas credenciais</h3>

    % if erro:
        <div class="warning">
            ⚠️ {{erro}}
        </div>
    % end
    
    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="email">📧 Email:</label>
            <input type="email" id="email" name="email" placeholder="seu@email.com" required>
        </div>
        
        <div class="form-group">
            <label for="senha">🔒 Senha:</label>
            <input type="password" id="senha" name="senha" placeholder="Digite sua senha" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>
        </div>
        
        <div class="form-actions">
            <button type="button" onclick="window.location.href='/signup'" class="btn-secondary">Criar uma conta</button>
        </div>
    </form>
</section>