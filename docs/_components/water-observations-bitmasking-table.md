<div class="scroll-horizontally">
    <table class="colour-coded-table dea-water-observations-bitflags">
        <caption>In this table, the grey boxes are impossible values that cannot occur. The yellow boxes are ???????. Notable crossover values include Cloudy Terrain (Cloud + High Slope; 64 + 16 = 80), Shady Water (Water + Cloud Shadow; 128 + 32 = 160), and Cloudy Water (Water + Cloud; 128 + 64 = 192).</caption>
        <thead>
            <tr>
                <th></th>
                <th></th>
                <th><strong>No Data</strong></th>
                <th><strong>Contiguity</strong></th>
                <th><strong>Low Solar Angle</strong></th>
                <th><strong>Terrain Shadow</strong></th>
                <th><strong>High Slope</strong></th>
                <th><strong>Cloud Shadow</strong></th>
                <th><strong>Cloud</strong></th>
                <th><strong>Cloudy Terrain</strong></th>
                <th><strong>Water</strong></th>
                <th><strong>Shady Water</strong></th>
                <th><strong>Cloudy Water</strong></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td></td>
                <td class="classification-decimal"></td>
                <td class="classification-decimal">1</td>
                <td class="classification-decimal">2</td>
                <td class="classification-decimal">4</td>
                <td class="classification-decimal">8</td>
                <td class="classification-decimal">16</td>
                <td class="classification-decimal">32</td>
                <td class="classification-decimal">64</td>
                <td class="classification-decimal">80</td>
                <td class="classification-decimal">128</td>
                <td class="classification-decimal">160</td>
                <td class="classification-decimal">192</td>
            </tr>
            <tr>
                <td><strong>No Data</strong></td>
                <td class="classification-decimal">1</td>
                <td class="impossible">2</td>
                <td class="impossible">3</td>
                <td class="impossible">5</td>
                <td class="impossible">9</td>
                <td class="impossible">17</td>
                <td class="impossible">33</td>
                <td class="impossible">65</td>
                <td class="impossible">81</td>
                <td class="impossible">129</td>
                <td class="impossible">161</td>
                <td class="impossible">193</td>
            </tr>
            <tr>
                <td><strong>Contiguity</strong></td>
                <td class="classification-decimal">2</td>
                <td class="impossible">3</td>
                <td class="impossible">4</td>
                <td class="impossible">6</td>
                <td class="impossible">10</td>
                <td class="impossible">18</td>
                <td class="impossible">34</td>
                <td class="impossible">66</td>
                <td class="impossible">82</td>
                <td class="impossible">130</td>
                <td class="impossible">162</td>
                <td class="impossible">194</td>
            </tr>
            <tr>
                <td><strong>Low Solar Angle</strong></td>
                <td class="classification-decimal">4</td>
                <td class="impossible">5</td>
                <td class="impossible">6</td>
                <td class="impossible">8</td>
                <td>12</td>
                <td>20</td>
                <td>36</td>
                <td>68</td>
                <td class="special">84</td>
                <td>132</td>
                <td>164</td>
                <td>196</td>
            </tr>
            <tr>
                <td><strong>Terrain Shadow</strong></td>
                <td class="classification-decimal">8</td>
                <td class="impossible">9</td>
                <td class="impossible">10</td>
                <td>12</td>
                <td class="impossible">16</td>
                <td>24</td>
                <td>40</td>
                <td>72</td>
                <td>88</td>
                <td>136</td>
                <td>168</td>
                <td>200</td>
            </tr>
            <tr>
                <td><strong>High Slope</strong></td>
                <td class="classification-decimal">16</td>
                <td class="impossible">17</td>
                <td class="impossible">18</td>
                <td>20</td>
                <td>24</td>
                <td class="impossible">32</td>
                <td>48</td>
                <td>80</td>
                <td>96</td>
                <td>144</td>
                <td>176</td>
                <td>208</td>
            </tr>
            <tr>
                <td><strong>Cloud Shadow</strong></td>
                <td class="classification-decimal">32</td>
                <td class="impossible">33</td>
                <td class="impossible">34</td>
                <td>36</td>
                <td>40</td>
                <td>48</td>
                <td class="impossible">64</td>
                <td>96</td>
                <td>112</td>
                <td>160</td>
                <td>192</td>
                <td>224</td>
            </tr>
            <tr>
                <td><strong>Cloud</strong></td>
                <td class="classification-decimal">64</td>
                <td class="impossible">65</td>
                <td class="impossible">66</td>
                <td>68</td>
                <td>72</td>
                <td>80</td>
                <td>96</td>
                <td class="impossible">128</td>
                <td class="impossible">144</td>
                <td>192</td>
                <td>224</td>
                <td class="impossible">256</td>
            </tr>
            <tr>
                <td><strong>Cloudy Terrain</strong></td>
                <td class="classification-decimal">80</td>
                <td class="impossible">81</td>
                <td class="impossible">82</td>
                <td class="special">84</td>
                <td>88</td>
                <td class="impossible">96</td>
                <td>112</td>
                <td>144</td>
                <td class="impossible">160</td>
                <td>208</td>
                <td>240</td>
                <td class="impossible">272</td>
            </tr>
            <tr>
                <td><strong>Water</strong></td>
                <td class="classification-decimal">128</td>
                <td class="impossible">129</td>
                <td class="impossible">130</td>
                <td>132</td>
                <td>136</td>
                <td>144</td>
                <td>160</td>
                <td>192</td>
                <td>208</td>
                <td class="impossible">256</td>
                <td class="impossible">288</td>
                <td class="impossible">320</td>
            </tr>
            <tr>
                <td><strong>Shady Water</strong></td>
                <td class="classification-decimal">160</td>
                <td class="impossible">161</td>
                <td class="impossible">162</td>
                <td>164</td>
                <td>168</td>
                <td>176</td>
                <td>192</td>
                <td>224</td>
                <td>240</td>
                <td class="impossible">288</td>
                <td class="impossible">320</td>
                <td class="impossible">352</td>
            </tr>
            <tr>
                <td><strong>Cloudy Water</strong></td>
                <td class="classification-decimal">192</td>
                <td class="impossible">193</td>
                <td class="impossible">194</td>
                <td>196</td>
                <td>200</td>
                <td>208</td>
                <td>224</td>
                <td class="impossible">256</td>
                <td class="impossible">272</td>
                <td class="impossible">320</td>
                <td class="impossible">352</td>
                <td class="impossible">384</td>
            </tr>
        </tbody>
    </table>
</div>
