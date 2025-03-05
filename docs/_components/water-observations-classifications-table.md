<div class="scroll-horizontally">
    <table>
        <caption>Classifications</caption>
        <thead>
            <tr>
                <th></th>
                <th></th>
                <th>Classification</th>
                <th>Bit flag</th>
                <th>Decimal</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>No data</strong></td>
                <td>0</td>
                <td>1</td>
                <td>Missing or invalid data. Pixel masked out due to NO_DATA in NBART source, 0 = valid data in NBART.</td>
            </tr>
            <tr>
                <td><strong>Contiguity</strong></td>
                <td>1</td>
                <td>2</td>
                <td>Some data is missing in the original image (usually missing bands). Pixel masked out due to lack of data contiguity.</td>
            </tr>
            <tr>
                <td><strong>Low solar angle</strong></td>
                <td>2</td>
                <td>4</td>
                <td>Also known as Solar Incidence. The angle of the sun can cast a large shadow which can be misclassified as water. Pixel masked out due to solar incidence of less than 10 degrees.</td>
            </tr>
            <tr>
                <td><strong>Terrain shadow</strong></td>
                <td>3</td>
                <td>8</td>
                <td>Topographic features can cast shadows which can be misclassified as water. Pixel masked out due to terrain shadow.</td>
            </tr>
            <tr>
                <td><strong>High slope</strong></td>
                <td>4</td>
                <td>16</td>
                <td>A highly sloped terrain is less likely to contain water, so therefore, a detection of water on this surface is often incorrect. Pixel masked out due to high slope.</td>
            </tr>
            <tr>
                <td><strong>Cloud shadow</strong></td>
                <td>5</td>
                <td>32</td>
                <td>Shadows are likely to be misclassified as water. Pixel masked out due to cloud shadow.</td>
            </tr>
            <tr>
                <td><strong>Cloud</strong></td>
                <td>6</td>
                <td>64</td>
                <td>Cloud is affecting the output data. Pixel masked out due to cloud.</td>
            </tr>
            <tr>
                <td><strong>Water</strong></td>
                <td>7</td>
                <td>128</td>
                <td>This pixel is classified as water.</td>
            </tr>
        </tbody>
    </table>
</div>

<br />
