export default function Video({ src }) {
    return (
        <div class="container-fluid">
        <video controls>
            <source src={src} type="video/mp4" />
            Sorry, your browser doesn't support videos.
        </video>
        </div>
   );
}
