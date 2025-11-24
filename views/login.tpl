% rebase('layout', title='Login')

<section class="form-section">
    <h1>{{'Login'}}</h1>

    % if erro:
        <div class="warning">
            <i>{{erro}}</i>
        </div>
    % end
    
    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>
            <button type="button" onclick="window.location.href='/signup'" class="btn-cancel">Sign-up</button>
        </div>
    </form>
</section>